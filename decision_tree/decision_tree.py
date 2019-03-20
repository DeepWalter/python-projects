import csv
import random


class Question:
    """A question is used to partition a dataset.

    Attributes
    ----------
    column: int
        column number of the feature
    value: int, float, or str
        the value used to decide the partition
    headers: list[str]
        list of names of the features (default to None)

    Methods
    -------
    match(example)
        Test whether the example matches the question.
    """

    def __init__(self, column, value, headers=None):
        self.column = column
        self.value = value
        self.headers = headers

    def match(self, example):
        """Test whether the example matches the question.

        Parameters
        ----------
        example: list
            an single instance to be tested

        Returns
        -------
        bool
            True if the example matches the question; False otherwise
        """
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

    def __repr__(self):
        """Print the question in a readable form."""
        condition = '=='
        header_name = f'headers[{self.column}]'
        if self.headers is not None:
            header_name = self.headers[self.column]
        if is_numeric(self.value):
            condition = '>='
        return f'Is {header_name} {condition} {self.value}?'


def is_numeric(val):
    """Whether val is a number."""
    return isinstance(val, int) or isinstance(val, float)


def partition(rows, question):
    """Partition rows according to question.

    Parameters
    ----------
    rows: list
        a list of instances
    question: Question
        the question used to do the partition

    Returns
    -------
    (list, list)
        a pair of lists. The left one is the list of true instances and
        the right one the list of false instances.
    """
    trues, falses = [], []
    for row in rows:
        if question.match(row):
            trues.append(row)
        else:
            falses.append(row)

    return trues, falses


def class_counts(rows):
    """Count the occurrence of each class in rows.

    Each element of rows is a tuple or list representing a single
    instance. We assume the last element of every instance is the class
    name (or the label).

    Parameters
    ----------
    rows: list
        a list of instances

    Returns
    -------
    dict
        statistics of the occurrences of classes in rows. The keys are
        the class names and the values are the corresponding number of
        occurrences.
    """
    counts = {}
    for row in rows:
        label = row[-1]
        counts[label] = counts.get(label, 0) + 1

    return counts


def gini(rows):
    """Compute the Gini index of rows according to its class names.

    Each element of rows is a tuple or list representing a single
    instance. We assume the last element of every instance is the class
    name (or the label).

    Parameters
    ----------
    rows: list
        a list of instances

    Returns
    -------
    float
        Gini index of rows according to its class names
    """
    counts = class_counts(rows)
    n_total = len(rows)
    gini_index = 1
    for label in counts:
        gini_index -= (counts[label] / n_total) ** 2

    return gini_index


def info_gain(trues, falses, current_gini):
    """Compute the information gain of splitting the current collection
    into left and right.

    Parameters
    ----------
    trues: list
        list of true instances after splitting
    falses: list
        list of false instances after splitting
    current_gini: float
        Gini index of current list

    Returns
    -------
    float
        Information gain
    """
    p = len(trues) / (len(trues) + len(falses))
    return current_gini - p * gini(trues) - (1 - p) * gini(falses)


def find_best_split(rows, headers=None):
    """Find the best question to split the rows.

    Iterate through every feature and value to find the best binary
    split.

    Parameters
    ----------
    rows: list
        a list of instances
    headers: list[str]
        list of names of the features (default to None)

    Returns
    -------
    (Question, float)
        the pair of best question and its corresponding information gain
    """
    best_gain = 0
    best_question = None
    current_gini = gini(rows)
    n_features = len(rows[0]) - 1

    for col in range(n_features):
        values = set([row[col] for row in rows])
        for val in values:
            question = Question(col, val, headers)
            trues, falses = partition(rows, question)

            # Sanity check.
            if len(trues) == 0 or len(falses) == 0:
                continue

            gain = info_gain(trues, falses, current_gini)

            if best_gain <= gain:
                best_question, best_gain = question, gain

    return best_question, best_gain


class Leaf:
    """A leaf node."""

    def __init__(self, rows):
        self.predictions = class_counts(rows)

    def __repr__(self):
        return str(self.predictions)

    def __str__(self):
        probs = {}
        total = sum(self.predictions.values())
        for key in self.predictions:
            probs[key] = f'{self.predictions[key] / total:.2%}'
        return str(probs)


class Node:
    """A decision node."""

    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

    def __repr__(self):
        return str(self.question)


def build_tree(rows, headers=None):
    """Build the binary decision tree.

    Parameters
    ----------
    rows: list
        a list of instances
    headers: list[str]
        list of names of the features (default to None)

    Returns
    -------
    Node
        the root node of the binary decision tree
    """
    question, gain = find_best_split(rows, headers)
    if gain == 0:
        return Leaf(rows)

    true_rows, false_rows = partition(rows, question)

    true_branch = build_tree(true_rows, headers)
    false_branch = build_tree(false_rows, headers)

    return Node(question, true_branch, false_branch)


def print_tree(node, spacing=''):
    """Print the tree.

    Parameters
    ----------
    node: Leaf or Node
        a tree or leaf node to be printed
    spacing: str
        spacing string
    """
    if isinstance(node, Leaf):
        print(spacing + 'Predict: ' + str(node))
        return

    print(spacing + str(node))  # Print question
    # Print true branch
    print(spacing + '-->True:')
    print_tree(node.true_branch, spacing + '    ')
    # Print false branch
    print(spacing + '-->False:')
    print_tree(node.false_branch, spacing + '    ')


def classify(row, node):
    """Classify an instance (row) according to the decision tree (tree).

    Parameters
    ----------
    row: list
        a single instance
    node: Leaf or Node
        the decision tree

    Returns
    -------
    Leaf
        the leaf in which the instance falls
    """
    if isinstance(node, Leaf):
        return node

    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)


def majority_vote(leaf):
    """Determine the class of the leaf by majority vote."""
    pred = leaf.predictions
    return max(pred, key=lambda elem: int(pred.get(elem)))


if __name__ == '__main__':

    # training_data = [
    #     ['Green', 3, 'Apple'],
    #     ['Yellow', 3, 'Apple'],
    #     ['Red', 1, 'Grape'],
    #     ['Red', 1, 'Grape'],
    #     ['Yellow', 3, 'Lemon'],
    #     ['Yellow', 1, 'Banana']
    # ]

    # headers = ['color', 'diameter', 'label']

    # leaf = Leaf(training_data)
    # tree = build_tree(training_data, headers)

    # for row in training_data:
    #     print(f'Actual: {row[-1]}. Predict: {classify(row, tree)}')
    iris_headers = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth',
                    'Class']

    with open('iris.csv') as f:
        irisreader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        iris_data = list(irisreader)

    random.shuffle(iris_data)
    n_train = int(len(iris_data) * 0.8)
    training_data = iris_data[:n_train]
    test_data = iris_data[n_train:]
    tree = build_tree(training_data, iris_headers)
    print_tree(tree)

    n_false = 0
    for row in test_data:
        prediction = majority_vote(classify(row, tree))
        if row[-1] != prediction:
            n_false += 1
    accuracy = 1 - n_false / len(test_data)

    print(f'Accuracy is {accuracy:.2%}')

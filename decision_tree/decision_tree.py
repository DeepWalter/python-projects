
class Question:
    """A question is used to partition a dataset.

    Parameters
    ----------
    column: int
        column number of the feature
    value: int, float, or str
        the value used to decide the partition
    headers: list[str]
        list of names of the features (default to None)
    """

    def __init__(self, column, value, headers=None):
        self.column = column
        self.value = value
        self.headers = headers

    def match(self, example):
        """Test whether the example mathes the question.

        Parameters
        ----------
        example: list
            an single instance to be tested

        Returns: bool
            True if the example mathes the question; False otherwise
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
    """Partition the rows according to the question.

    Parameters
    ----------
    rows: list
        a collection of instances
    question: Question
        the question used to do the partition

    Returns
    -------
    (list, list)
        a pair of lists. The left one is the collection of true instances and
        the right one the collection of false instances.
    """
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)

    return true_rows, false_rows


def class_counts(rows):
    """Count the occurrence of each class in rows.

    Each element of rows is a tuple or list representing a single
    instance. We assume the last element of every instance is the class
    name (or the label).

    Parameters
    ----------
    rows: list
        a collection of instances

    Returns
    -------
    dict
        a dictionary with class names as its keys and number of class
        occurrences as its corresponding values
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
        a collection of instances

    Returns
    -------
    float
        the Gini index of rows according to its class names
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
        collection of true instances after splitting
    falses: list
        collection of false instances after splitting
    current_gini: float
        Gini index of current collection

    Returns
    -------
    float
        Information gain
    """
    p = len(trues) / (len(trues) + len(falses))
    return current_gini - p * gini(trues) - (1 - p) * gini(falses)


def find_best_split(rows, headers=None):
    """Find the best question to split the rows.

    Parameters
    ----------
    rows: list
        a collection of instances
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
            gain = info_gain(trues, falses, current_gini)

            if best_gain <= gain:
                best_question, best_gain = question, gain

    return best_question, best_gain


if __name__ == '__main__':

    training_data = [
        ['Green', 3, 'Apple'],
        ['Yellow', 3, 'Apple'],
        ['Red', 1, 'Grape'],
        ['Red', 1, 'Grape'],
        ['Yellow', 3, 'Lemon'],
    ]

    headers = ['color', 'diameter', 'label']

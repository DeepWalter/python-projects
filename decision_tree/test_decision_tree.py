import unittest

from decision_tree import is_numeric
from decision_tree import Question
from decision_tree import partition
from decision_tree import class_counts
from decision_tree import gini
from decision_tree import info_gain


class TestIsNumeric(unittest.TestCase):
    def test_int(self):
        self.assertTrue(is_numeric(1))

    def test_float(self):
        self.assertTrue(is_numeric(1.1))

    def test_str(self):
        self.assertFalse(is_numeric('hello'))


class TestQuestion(unittest.TestCase):
    def setUp(self):
        headers = ['color', 'diameter', 'label']
        self.question = Question(0, 'Green', headers)

    def test_math(self):
        example = ['Green', 3, 'Apple']
        self.assertTrue(self.question.match(example))

    def test_question(self):
        self.assertEqual(str(self.question), 'Is color == Green?')


class TestPartition(unittest.TestCase):

    def setUp(self):
        self.rows = [
            ['Green', 3, 'Apple'],
            ['Yellow', 3, 'Apple'],
            ['Red', 1, 'Grape'],
            ['Red', 1, 'Grape'],
            ['Yellow', 3, 'Lemon'],
        ]

    def test_partition(self):
        question = Question(0, 'Red')
        true_rows, false_rows = partition(self.rows, question)

        self.assertEqual(true_rows,
                         [['Red', 1, 'Grape'],
                          ['Red', 1, 'Grape']],
                         msg='true_rows error')
        self.assertEqual(false_rows,
                         [['Green', 3, 'Apple'],
                          ['Yellow', 3, 'Apple'],
                          ['Yellow', 3, 'Lemon']],
                         msg='false_row error')


class TestClassCounts(unittest.TestCase):
    def setUp(self):
        self.data = [
            ['Green', 3, 'Apple'],
            ['Yellow', 3, 'Apple'],
            ['Red', 1, 'Grape'],
            ['Red', 1, 'Grape'],
            ['Yellow', 3, 'Lemon'],
        ]

    def test_class_counts(self):
        counts = class_counts(self.data)
        self.assertEqual(counts, {'Apple': 2, 'Grape': 2, 'Lemon': 1})


class TestGini(unittest.TestCase):

    def test_pure(self):
        pure = [['apple'], ['apple']]
        self.assertEqual(gini(pure), 0.0)

    def test_mixed(self):
        mixed = [['apple'], ['pear']]
        self.assertEqual(gini(mixed), 0.5)

    def test_info_gain(self):
        data = [
            ['Green', 3, 'Apple'],
            ['Yellow', 3, 'Apple'],
            ['Red', 1, 'Grape'],
            ['Red', 1, 'Grape'],
            ['Yellow', 3, 'Lemon'],
        ]
        question = Question(0, 'Red')
        trues, falses = partition(data, question)
        self.assertEqual(info_gain(trues, falses, gini(data)),
                         0.37333333333333324)


if __name__ == '__main__':
    unittest.main()

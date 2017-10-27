from unittest import TestCase
from snail import (
    Snail,
    InvalidParameterError
)


class SnailTest(TestCase):

    def test_it_raises_InvalidParameterError_with_empty_array(self):
        with self.assertRaises(InvalidParameterError):
            Snail([])

    def test_it_raises_InvalidParameterError_with_none_square_array(self):
        with self.assertRaises(InvalidParameterError):
            Snail([[2, 0]])

    def test_it_raises_InvalidParameterError_with_string(self):
        with self.assertRaises(InvalidParameterError):
            Snail('a')

    def test_it_raises_InvalidParameterError_with_string_in_array(self):
        with self.assertRaises(InvalidParameterError):
            Snail([[1, 1], [2, 'a']])

    def test_when_square_1x1_result_is_its_value(self):
        snail = Snail([[3]])

        self.assertEqual(snail.process(), [3])

    def test_when_square_2x2_result_is_its_values_in_snail_order(self):
        snail = Snail([[4, 2], [1, 5]])

        self.assertEqual(snail.process(), [4, 2, 5, 1])

    # def test_when_square_3x3_result_is_its_values_in_snail_order(self):
    #     snail = Snail([[4, 2, 9], [1, 5, 5], [5, 4, 6]])

    #     self.assertEqual(snail.process(), [4, 2, 9, 5, 6, 4, 5, 1, 5])


class TruncateArrayTest(TestCase):
    def test_when_square_2x2_result_is_first_row_and_last_column(self):
        snail = Snail([[4, 2], [1, 5]])

        self.assertEqual(snail.truncateArray([]), [4, 2, 5])


class ReverseArrayTest(TestCase):
    def test_when_square_2x2_result_is_reversed_array(self):
        snail = Snail([[4, 2], [1, 5]])
        snail.reverseArray()

        self.assertEqual(snail.data, [[5, 1], [2, 4]])

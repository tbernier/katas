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

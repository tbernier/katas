from unittest import TestCase
from howmanynumbers import (
    HowManyNumbers,
    InvalidParameterError
)


class HowManyNumbersTest(TestCase):
    def test_it_raises_InvalidParameterError_when_total_is_not_integer(self):
        with self.assertRaises(InvalidParameterError):
            HowManyNumbers(total='a')

    def test_it_raises_InvalidParameterError_when_total_is_not_greater_than_0(
            self):
        with self.assertRaises(InvalidParameterError):
            HowManyNumbers(total=0)

    def test_it_raises_InvalidParameterError_when_digits_is_not_integer(self):
        with self.assertRaises(InvalidParameterError):
            HowManyNumbers(digit='a')

    def test_it_raises_InvalidParameterError_when_digit_is_not_greater_than_0(
            self):
        with self.assertRaises(InvalidParameterError):
            HowManyNumbers(digit=0)


class HowManyNumbersProcessTest(TestCase):

    def test_it_return_1_1_1_with_total_1_digit_1(self):
        howmanynumbers = HowManyNumbers(1, 1)

        self.assertEqual(howmanynumbers.process(), [1, 1, 1])

    def test_it_return_1_2_2_with_total_2_digit_1(self):
        howmanynumbers = HowManyNumbers(2, 1)

        self.assertEqual(howmanynumbers.process(), [1, 2, 2])

    def test_it_return_empty_array_with_total_1_digit_2(self):
        howmanynumbers = HowManyNumbers(1, 2)

        self.assertEqual(howmanynumbers.process(), [])

    def test_it_return_empty_array_with_total_10_digit_1(self):
        howmanynumbers = HowManyNumbers(10, 1)

        self.assertEqual(howmanynumbers.process(), [])

    def test_it_return_1_11_11_with_total_2_digit_2(self):
        howmanynumbers = HowManyNumbers(2, 2)

        self.assertEqual(howmanynumbers.process(), [1, 11, 11])

    def test_it_return_1_12_12_with_total_3_digit_2(self):
        howmanynumbers = HowManyNumbers(3, 2)

        self.assertEqual(howmanynumbers.process(), [1, 12, 12])

    def test_it_return_2_13_22_with_total_4_digit_2(self):
        howmanynumbers = HowManyNumbers(4, 2)

        self.assertEqual(howmanynumbers.process(), [2, 13, 22])

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

    def test_it_return_1_112_112_with_total_4_digit_3(self):
        howmanynumbers = HowManyNumbers(4, 3)

        self.assertEqual(howmanynumbers.process(), [1, 112, 112])

    def test_it_return_3_114_222_with_total_6_digit_3(self):
        howmanynumbers = HowManyNumbers(6, 3)

        self.assertEqual(howmanynumbers.process(), [3, 114, 222])

    def test_it_return_4_115_223_with_total_7_digit_3(self):
        howmanynumbers = HowManyNumbers(7, 3)

        self.assertEqual(howmanynumbers.process(), [4, 115, 223])

    def test_it_return_7_117_333_with_total_9_digit_3(self):
        howmanynumbers = HowManyNumbers(9, 3)

        self.assertEqual(howmanynumbers.process(), [7, 117, 333])

    def test_it_return_11_129_444_with_total_12_digit_3(self):
        howmanynumbers = HowManyNumbers(12, 3)

        self.assertEqual(howmanynumbers.process(), [11, 129, 444])

    def test_it_return_2_699_888_with_total_24_digit_3(self):
        howmanynumbers = HowManyNumbers(24, 3)

        self.assertEqual(howmanynumbers.process(), [3, 699, 888])

    def test_it_return_8_118_334_with_total_10_digit_3(self):
        howmanynumbers = HowManyNumbers(10, 3)

        self.assertEqual(howmanynumbers.process(), [8, 118, 334])

    def test_it_return_3_1114_1222_with_total_7_digit_4(self):
        howmanynumbers = HowManyNumbers(7, 4)

        self.assertEqual(howmanynumbers.process(), [3, 1114, 1222])

    def test_it_return_123_116999_566666_with_total_35_digit_6(self):
        howmanynumbers = HowManyNumbers(35, 6)

        self.assertEqual(howmanynumbers.process(), [123, 116999, 566666])

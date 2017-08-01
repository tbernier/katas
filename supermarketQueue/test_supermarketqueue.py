from unittest import TestCase
from supermarketqueue import (
    SupermarketQueue,
    NoTillsError,
    InvalidCustomer
)


class SupermarketQueueTest(TestCase):

    def test_return_zero_without_customers(self):
        queue = SupermarketQueue()

        self.assertEquals(queue.process(), 0)

    def test_it_raises_no_tills_exception_without_tills(self):
        with self.assertRaises(NoTillsError):
            SupermarketQueue(customers=[1], tills=0)

    def test_it_raises_invalid_customer_with_negativ_customer(self):
        with self.assertRaises(InvalidCustomer):
            SupermarketQueue(customers=[-1])

    def test_it_raises_invalid_customer_with_string_customer(self):
        with self.assertRaises(InvalidCustomer):
            SupermarketQueue(customers=['foo'])

    def test_it_returns_1_with_minimal_values(self):
        queue = SupermarketQueue([1], 1)

        self.assertEquals(queue.process(), 1)

    def test_it_returns_2_with_one_2min_customer(self):
        queue = SupermarketQueue([2], 1)

        self.assertEquals(queue.process(), 2)

    def test_it_returns_2_with_two_1min_customers(self):
        queue = SupermarketQueue([1, 1], 1)

        self.assertEquals(queue.process(), 2)

    def test_it_returns_1_with_two_1min_customers_and_2_tills(self):
        queue = SupermarketQueue([1, 1], 2)

        self.assertEquals(queue.process(), 1)

    def test_it_returns_10_with_many_customers_and_2_tills(self):
        queue = SupermarketQueue([10, 2, 3, 3], 2)

        self.assertEquals(queue.process(), 10)

    def test_it_returns_12_with_many_customers_and_2tills(self):
        queue = SupermarketQueue([2, 3, 10], 2)

        self.assertEquals(queue.process(), 12)

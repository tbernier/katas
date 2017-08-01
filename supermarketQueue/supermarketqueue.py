class SupermarketQueue:

    def __init__(self, customers=[], tills=1):
        self.customers = customers
        self.tills = tills

        for customer in self.customers:
            if not isinstance(customer, int):
                raise InvalidCustomer

            if customer < 0:
                raise InvalidCustomer

        if self.tills == 0:
            raise NoTillsError

    def process(self):
        if self.customers == []:
            return 0

        queue = []

        for index in range(0, self.tills):
            queue.append(0)

        for customer in self.customers:
            queue.sort()
            queue[0] += customer

        queue.sort(reverse=True)
        return queue[0]


def queue_time(customers, n):
    return SupermarketQueue(customers, n).process()


class NoTillsError(Exception):
    pass


class InvalidCustomer(Exception):
    pass

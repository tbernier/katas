class HowManyNumbers:

    def __init__(self, total=1, digit=1):
        self.total = total
        self.digit = digit
        self.results = []

        if not isinstance(self.total, int) or not isinstance(self.digit, int):
            raise InvalidParameterError

        if self.total <= 0 or self.digit <= 0:
            raise InvalidParameterError

    def process(self):

        if self.total < self.digit:
            return self.results

        if self.total > self.digit * 9:
            return self.results

        if self.total == self.digit:
            return [1, int("1" * self.digit), int("1" * self.digit)]

        buffer = []
        for x in range(1, self.total):
            # recursif incomming
            if self.digit == 2:
                buffer.append(str(x) + str(self.total - x))
            else:
                buffer.append(str(self.total))

        for i in buffer:
            self.results.append(int(''.join(sorted(i))))

        self.results = list(set(self.results))

        return [
            len(self.results),
            self.results[0],
            self.results[-1]
        ]


class InvalidParameterError(Exception):
    pass

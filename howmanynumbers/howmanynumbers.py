class HowManyNumbers:

    def __init__(self, total=1, digit=1):
        self.total = total
        self.digit = digit
        self.buffer = []
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

        self.cutInTwo(self.total, self.digit, '')

        for i in self.buffer:
            self.results.append(int(''.join(sorted(i))))

        self.results = list(set(self.results))

        return [
            len(self.results),
            self.results[0],
            self.results[-1]
        ]

    def cutInTwo(self, total, digit, prepend):

        if digit == 1:
            self.buffer.append(str(total))
        elif digit == 2:
            for x in range(1, total):
                self.buffer.append(str(prepend) + str(x) + str(total - x))
        else:
            for x in range(1, (total - digit)):
                self.cutInTwo(total - x, digit - 1, x)


class InvalidParameterError(Exception):
    pass

class HowManyNumbers:

    def __init__(self, total=1, digit=1):
        self.total = total
        self.digit = digit

        if not isinstance(self.total, int) or not isinstance(self.digit, int):
            raise InvalidParameterError

        if self.total <= 0 or self.digit <= 0:
            raise InvalidParameterError

    def process(self):
        # to remove
        start = "".rjust(self.digit, 1)
        end = "".rjust(self.digit, 9)


        return [1, self.total, self.total]


class InvalidParameterError(Exception):
    pass

class Snail:

    def __init__(self, data):

        self.data = data

        if not isinstance(data, list):
            raise InvalidParameterError

        if self.data == []:
            raise InvalidParameterError

        for line in self.data:
            if len(line) != len(data):
                raise InvalidParameterError

            for value in line:
                if not isinstance(value, int):
                    raise InvalidParameterError

        self.process()

    def process(self):
        return [3]


class InvalidParameterError(Exception):
    pass

class Snail:

    def __init__(self, data):

        self.data = data

        if not isinstance(self.data, list):
            raise InvalidParameterError

        if self.data == []:
            raise InvalidParameterError

        for line in self.data:
            if len(line) != len(self.data):
                raise InvalidParameterError

            for value in line:
                if not isinstance(value, int):
                    raise InvalidParameterError

        self.process()

    def process(self):
        result = []

        if len(self.data) == 1:
            return self.data[0]

        result.append(self.data[0][0])
        result.append(self.data[0][1])
        result.append(self.data[1][1])
        result.append(self.data[1][0])

        return result

    def truncateArray(self, result):
        for value in self.data.pop(0):
            result.append(value)

        for line in self.data:
            result.append(line.pop())

        return result

    def reverseArray(self):
        self.data.reverse()

        for i in range(0, len(self.data)):
            self.data[i].reverse()


class InvalidParameterError(Exception):
    pass

class Snail:

    def __init__(self, data):

        self.data = data

        if not isinstance(self.data, list):
            raise InvalidParameterError

        if self.data == []:
            raise InvalidParameterError

        if self.data != [[]]:
            for line in self.data:
                if len(line) != len(self.data):
                    raise InvalidParameterError

                for value in line:
                    if not isinstance(value, int):
                        raise InvalidParameterError

    def process(self):
        result = []

        while len(self.data):
            self.data, result = truncateArray(self.data, result)

        return result


def truncateArray(data, result):
    for value in data.pop(0):
        result.append(value)

    for line in data:
        result.append(line.pop())

    return reverseArray(data), result


def reverseArray(data):
    data.reverse()

    for i in range(0, len(data)):
        data[i].reverse()

    return data


class InvalidParameterError(Exception):
    pass

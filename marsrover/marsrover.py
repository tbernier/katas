class Orientation(object):
    east = 'E'
    north = 'N'
    south = 'S'
    west = 'W'

    @classmethod
    def get_all(cls):
        return [
            getattr(cls, p)
            for p in dir(cls)
            if isinstance(getattr(cls, p), str)
        ]


class Order(object):
    backward = 'b'
    forward = 'f'
    left = 'l'
    right = 'r'

    @classmethod
    def get_all(cls):
        return [
            getattr(cls, p)
            for p in dir(cls)
            if isinstance(getattr(cls, p), str)
        ]


class MarsRover:

    limit_x = 100
    limit_y = 100
    vectors = {
        Orientation.north: (0, 1),
        Orientation.east: (1, 0),
        Orientation.south: (0, -1),
        Orientation.west: (-1, 0)
    }

    def __init__(self, x=0, y=0, orientation=Orientation.north,
                 orders=[], rocks=[]):
        check_position_parameters(x, y)
        check_orientation_parameter(orientation)
        check_order_parameter(orders)

        self.x = x
        self.y = y
        self.orientation = orientation
        self.cardinals = list(self.vectors.keys())
        self.rocks = rocks

        for order in orders:
            self.execute(order)

    @property
    def position(self):
        return (self.x, self.y)

    def execute(self, order):
        if order in [Order.forward, Order.backward]:
            self._move(order)
        else:
            self._rotate(order)

    def _move(self, order):
        vector = self.vectors[self.orientation]
        ratio = 1 if order == Order.forward else -1

        x = self.x + vector[0] * ratio
        y = self.y + vector[1] * ratio

        (x, y) = self._check_borders(x, y)

        if (x, y) in self.rocks:
            raise ReachedObstacleError()

        self.x = x
        self.y = y

    def _rotate(self, order):
        posinit = self.cardinals.index(self.orientation)
        if order == Order.right:
            self.orientation = self.cardinals[
                (posinit + 1) % len(self.cardinals)]
        else:
            self.orientation = self.cardinals[posinit - 1]

    def _check_borders(self, x, y):
        dic = {'x': x, 'y': y}
        for axis, position in dic.items():
            my_axis = position
            limit = getattr(self, 'limit_{}'.format(axis))
            if my_axis > limit:
                dic[axis] = 0

            if my_axis < 0:
                dic[axis] = limit

        return (dic['x'], dic['y'])


def check_position_parameters(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        raise InvalidParameterError()


def check_orientation_parameter(orientation):
    if orientation not in Orientation.get_all():
        raise InvalidParameterError()


def check_order_parameter(orders):
    if not isinstance(orders, list):
        raise ParameterTypeError()

    for order in orders:
        if order not in Order.get_all():
            raise InvalidParameterError()


class InvalidParameterError(Exception):
    pass


class ReachedObstacleError(Exception):
    pass


class ParameterTypeError(InvalidParameterError):
    pass

from unittest import TestCase
from unittest.mock import patch
from marsrover import (
    __name__ as tested_module_name,
    MarsRover,
    InvalidParameterError,
    ReachedObstacleError,
    ParameterTypeError,
    check_position_parameters,
    check_orientation_parameter,
    check_order_parameter
)


class MarsRoverTest(TestCase):

    def patch(self, object_name):
        patcher = patch('%s.%s' % (tested_module_name, object_name))

        self.addCleanup(patcher.stop)

        return patcher.start()

    def test_it_starts_at_0_0(self):
        marsrover = MarsRover()

        self.assertEquals(marsrover.position, (0, 0))

    def test_it_takes_starting_position(self):
        marsrover = MarsRover(3, 2)

        self.assertEquals(marsrover.position, (3, 2))

    def test_it_starts_facing_north(self):
        marsrover = MarsRover()

        self.assertEquals(marsrover.orientation, 'N')

    def test_it_takes_starting_orientation(self):
        marsrover = MarsRover(orientation='S')

        self.assertEquals(marsrover.orientation, 'S')

    def test_it_calls_check_position_parameters(self):
        patched_check = self.patch('check_position_parameters')

        MarsRover()

        self.assertTrue(patched_check.called)

    def test_it_calls_check_orientation_parameter(self):
        patched_check = self.patch('check_orientation_parameter')

        MarsRover()

        self.assertTrue(patched_check.called)

    def test_it_calls_check_order_parameter(self):
        patched_check = self.patch('check_order_parameter')

        MarsRover()

        self.assertTrue(patched_check.called)

    def test_it_calls_execute_with_orders(self):
        execute = self.patch('MarsRover.execute')

        MarsRover(orders=['f'])

        execute.assert_called_with('f')

    def test_it_works_when_lot_of_orders_given(self):
        marsrover = MarsRover(orders=[
            'f', 'f', 'r', 'f', 'f', 'l', 'b', 'b'
        ])

        self.assertEqual(marsrover.position, (2, 0))

    def test_it_returns_to_0_when_y_limit_is_crossed(self):
        marsrover = MarsRover(y=100, orders=['f'])

        self.assertEqual(marsrover.position, (0, 0))

    def test_it_returns_to_0_when_x_limit_is_crossed(self):
        marsrover = MarsRover(x=100, orientation='E', orders=['f'])

        self.assertEqual(marsrover.position, (0, 0))

    def test_it_returns_to_100_when_y_limit_is_crossed(self):
        marsrover = MarsRover(y=0, orders=['b'])

        self.assertEqual(marsrover.position, (0, 100))

    def test_it_returns_to_100_when_x_limit_is_crossed(self):
        marsrover = MarsRover(x=0, orientation='E', orders=['b'])

        self.assertEqual(marsrover.position, (100, 0))

    def test_it_raises_exception_when_reaching_obstacle(self):
        with self.assertRaises(ReachedObstacleError):
            MarsRover(orders=['f'], rocks=[(0, 1)])

    def test_it_stops_before_reaching_obstacle(self):
        marsrover = MarsRover(rocks=[(0, 1)])
        try:
            marsrover.execute('f')
            marsrover.execute('r')
            marsrover.execute('f')
        except ReachedObstacleError:
            pass

        self.assertEqual(marsrover.position, (0, 0))

    def test_it_stops_before_reaching_distant_obstacle(self):
        marsrover = MarsRover(rocks=[(0, 2)])
        try:
            marsrover.execute('f')
            marsrover.execute('f')
        except ReachedObstacleError:
            pass

        self.assertEqual(marsrover.position, (0, 1))

    def test_it_raises_exception_when_reaching_obstacle_and_limit_north(self):
        with self.assertRaises(ReachedObstacleError):
            MarsRover(y=100, orders=['f'], rocks=[(0, 0)])

    def test_raises_exception_when_reaching_obstacle_and_limit_west(self):
        with self.assertRaises(ReachedObstacleError):
            MarsRover(orientation='W', orders=['f'], rocks=[(100, 0)])


class MarsRoverMovesTest(TestCase):

    def test_it_moves_front_when_order_is_f(self):
        marsrover = MarsRover()

        marsrover.execute('f')

        self.assertEquals(marsrover.position, (0, 1))

    def test_it_moves_back_when_order_is_b(self):
        marsrover = MarsRover(y=1)

        marsrover.execute('b')

        self.assertEquals(marsrover.position, (0, 0))

    def test_it_turns_right_when_order_is_r(self):
        marsrover = MarsRover()

        marsrover.execute('r')

        self.assertEquals(marsrover.orientation, 'E')

    def test_it_turns_left_when_order_is_l(self):
        marsrover = MarsRover()

        marsrover.execute('l')

        self.assertEquals(marsrover.orientation, 'W')

    def test_it_moves_front_when_order_is_f_and_orientation_is_e(self):
        marsrover = MarsRover(orientation='E')

        marsrover.execute('f')

        self.assertEquals(marsrover.position, (1, 0))

    def test_it_moves_front_when_order_is_f_and_orientation_is_w(self):
        marsrover = MarsRover(orientation='W', x=1)

        marsrover.execute('f')

        self.assertEquals(marsrover.position, (0, 0))

    def test_it_moves_back_when_order_is_b_and_orientation_is_e(self):
        marsrover = MarsRover(orientation='E', x=1)

        marsrover.execute('b')

        self.assertEquals(marsrover.position, (0, 0))

    def test_it_rotate_to_south_when_order_is_r_and_orientation_is_e(self):
        marsrover = MarsRover(orientation='E')

        marsrover.execute('r')

        self.assertEqual(marsrover.orientation, 'S')

    def test_it_rotate_to_west_when_order_is_r_and_orientation_is_s(self):
        marsrover = MarsRover(orientation='S')

        marsrover.execute('r')

        self.assertEqual(marsrover.orientation, 'W')

    def test_it_rotate_to_north_when_order_is_r_and_orientation_is_w(self):
        marsrover = MarsRover(orientation='W')

        marsrover.execute('r')

        self.assertEqual(marsrover.orientation, 'N')

    def test_it_rotate_to_west_when_order_is_l_and_orientation_is_n(self):
        marsrover = MarsRover(orientation='N')

        marsrover.execute('l')

        self.assertEqual(marsrover.orientation, 'W')


class CheckParametersTypeTest(TestCase):

    def test_if_x_is_not_integer_it_raises_error(self):
        with self.assertRaises(InvalidParameterError):
            check_position_parameters('toto', 0)

    def test_if_y_is_not_integer_it_raises_error(self):
        with self.assertRaises(InvalidParameterError):
            check_position_parameters(0, 'toto')


class CheckOrientationParameterTest(TestCase):

    def test_orientation_not_valid_raises_error(self):
        with self.assertRaises(InvalidParameterError):
            check_orientation_parameter('foo')


class CheckOrderValidityTest(TestCase):

    def test_when_order_is_not_a_list_it_raises_error(self):
        with self.assertRaises(ParameterTypeError):
            check_order_parameter('foo')

    def test_order_not_valid_raises_error(self):
        with self.assertRaises(InvalidParameterError):
            check_order_parameter(['foo'])

    def test_order_valid_dont_raises_error(self):
        check_order_parameter(['f'])

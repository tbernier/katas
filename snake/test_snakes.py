from unittest import TestCase
from snakes import SnakesLadders, InvalidDie, check_dices, check_throw


class SnakesLaddersTest(TestCase):

    def setUp(self):
        self.game = SnakesLadders()

    def test_game_player1_starts_cell1(self):
        self.assertEqual(self.game.player1, 0)

    def test_game_player2_starts_cell1(self):
        self.assertEqual(self.game.player2, 0)

    def test_player1_starts(self):
        self.assertEqual(self.game.turn, 1)

    def test_game_has_action(self):
        self.assertIsInstance(self.game.actions, dict)


class CheckDicesTest(TestCase):

    def test_when_missing_dies_it_returns_false(self):
        self.assertFalse(check_dices(7, 7))

    def test_when_dies_are_not_between_1_and_6_it_returns_false(self):
        self.assertFalse(check_dices(0, 7))

    def test_when_dies_are_6_and_6_it_returns_true(self):
        self.assertTrue(check_dices(6, 6))

    def test_when_dies_are_4_and_6_it_returns_true(self):
        self.assertTrue(check_dices(4, 6))

class ReboundTest(TestCase):

    def test_if_105_then_returns_95(self):
        self.assertEqual(check_throw(105), 95)
    
    def test_if_95_then_returns_95(self):
        self.assertEqual(check_throw(95), 95)

class SnakesLaddersPlayTest(TestCase):

    def setUp(self):
        self.game = SnakesLadders()

    def test_when_missing_dies_it_raises_invalid_die_error(self):
        with self.assertRaises(InvalidDie):
            self.game.play()

    def test_dies_not_between_1_and_6_raises_invalid_die_error(self):
        with self.assertRaises(InvalidDie):
            self.game.play(0, 7)

    def test_player_1_roll_1_and_2_he_moves_to_cell_3(self):
        self.game.play(1, 2)

        self.assertEqual(self.game.player1, 3)

    def test_player_1_roll_1_and_1_he_moves_to_cell_38(self):
        self.game.play(1, 1)

        self.assertEqual(self.game.player1, 38)

    def test_player_1_lands_on_cell_16_he_moves_to_cell_6(self):
        self.game.player1 = 14
        print(self.game.__dict__)
        self.game.play(1, 1)
        print(self.game.__dict__)

        self.assertEqual(self.game.player1, 6)

    def test_after_player1_moves_turn_pass_to_player2(self):
        self.game.play(1, 2)

        self.assertEqual(self.game.turn, 2)

    def test_after_player2_moves_turn_pass_to_player1(self):
        self.game.turn = 2

        self.game.play(1, 2)

        self.assertEqual(self.game.turn, 1)

    def test_player_2_roll_1_and_2_he_moves_to_cell_3(self):
        self.game.turn = 2

        self.game.play(1, 2)

        self.assertEqual(self.game.player2, 3)

    def test_if_dices_are_equals_dont_change_player(self):
        self.game.play(1, 1)

        self.assertEqual(self.game.turn, 1)

    def test_if_greater_than_100_goes_backward(self):
        self.game.player1 = 97

        self.game.play(2, 5)

        self.assertEqual(self.game.player1, 96)

    def test_if_player1_reaches_100_then_wins(self):
        self.game.player1 = 98

        self.assertEqual(
            self.game.play(1, 1),
            "Youpi, player1 wins"
        )
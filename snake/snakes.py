class SnakesLadders():

    actions = {
        2: 38, 7: 14, 8: 31, 15: 26,
        16: 6, 21: 42, 28: 84, 36: 44,
        46: 25, 49: 11, 51: 67, 62: 19,
        64: 60, 71: 91, 74: 53, 78: 98,
        87: 94, 89: 68, 92: 88, 95: 75, 99: 80
    }

    def __init__(self):
        self.player1 = 0
        self.player2 = 0
        self.turn = 1

    @property
    def current_player(self):
        return "player%s" % self.turn

    def play(self, die1=None, die2=None):
        if not check_dices(die1, die2):
            raise InvalidDie()

        checked_throw = check_throw(
            getattr(self, self.current_player) + die1 + die2
        )

        player_cell = self.set_new_cell(checked_throw)

        if player_cell == 100:
            return "Youpi, player%s wins" % self.turn

        if player_cell in self.actions:
            self.set_new_cell(self.actions[player_cell])
            
        if die1 != die2:
            self.turn = 2 if self.turn == 1 else 1

    def set_new_cell(self, new_cell):
        setattr(self, self.current_player, new_cell)
        return getattr(self, self.current_player)

def check_throw(position):
    if position > 100:
        return 100 - (position - 100)
    return position

def check_dices(die1, die2):
    return die1 in range(1, 7) and die2 in range(1, 7)


class InvalidDie(Exception): 
    pass
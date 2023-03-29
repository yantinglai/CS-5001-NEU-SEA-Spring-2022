"""A pair of dice"""
from die import Die


class PairOfDice:
    """A pair of dice class"""
    def __init__(self):
        # two Die class attributes
        self.die1 = Die()
        self.die2 = Die()
        self.sum = sum

    def roll_dice(self):
        """roll two dice"""
        self.die1.roll()
        self.die2.roll()

    def current_value(self):
        """return the sum of two dies' current values"""
        self.sum = self.die1.current_value + self.die2.current_value
        return sum

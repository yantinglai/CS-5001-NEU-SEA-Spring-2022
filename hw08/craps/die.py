"""Construct a die"""
from random import randint


class Die:
    """A class of die"""
    def __init__(self):
        """Initialize the dice value"""
        self.current_value = 0  # 是否需要创建一个list来记录current value？

    def roll(self):
        """Get random number from 1 to 6"""
        ROLL_RANGE = (1, 6)
        self.current_value = randint(*ROLL_RANGE)

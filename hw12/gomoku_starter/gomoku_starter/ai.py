from board import Board
import random


class Ai:
    """An Ai Class"""
    def __init__(self):
        self.list = []  # create a list to record all the potention coordinates
        self.N = 14

    def get_random_coordinate(self):
        """Generate random coordinates for ai to put its stone"""
        row = random.randint(0, self.N)
        col = random.randint(0, self.N)
        return [row, col]

    # The functions below are for future implementation if given more time
    def choose_direction(self):
        pass
    # identify where are the 0 unoccupied columns
    # check occupancy of the 8 directions aournd the stone
    # if so, this spot is okay to put the white stone

    # Once we generate a list of eight coordinates
    # Check the score of each one
    # Return the coordinate with the best score
    def check_score(self):
        pass

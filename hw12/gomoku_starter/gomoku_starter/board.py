class Board:
    """A board class"""
    def __init__(self):
        self.rows = 15
        self.cols = 15
        self.board = [[0 for j in range(15)] for i in range(15)]
        self.SIZE = 900
        self.SPACING = self.SIZE // self.rows
        self.res = 0

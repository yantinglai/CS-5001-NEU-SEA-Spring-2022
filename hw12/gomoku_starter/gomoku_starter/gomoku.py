from board import Board
from stone import Stone
from ai import Ai


class Gomoku:

    def __init__(self):
        self.board = Board()
        self.ai = Ai()
        self.black = Stone(0, 0, 0)  # coordinate and color
        self.white = Stone(255, 0, 0)  # coordinate and color
        self.SPACING = 900 // 15
        self.size = 15
        self.bound1 = 15
        self.bound2 = 11
        self.count = 0
        self.list_of_names = {}  # keep record of the winners
        self.end = False

    def check_winner(self):
        """
        0: game continues
        1: human wins
        2: ai wins
        3: a tie
        """
        flag = self.isFull()
        if not flag:
            # check horizontally
            for i in range(self.bound1):
                for j in range(self.bound2):
                    if (self.board.board[i][j] == self.board.board[i][j+1]
                            == self.board.board[i][j+2]
                            == self.board.board[i][j+3]
                            == self.board.board[i][j+4]
                            == 1):  # human wins
                        return 1

                    elif (self.board.board[i][j] == self.board.board[i][j+1]
                            == self.board.board[i][j+2]
                            == self.board.board[i][j+3]
                            == self.board.board[i][j+4]
                            == 2):  # ai wins
                        return 2

            # check vertically
            for i in range(self.bound2):
                for j in range(self.bound1):
                    if (self.board.board[i][j] == self.board.board[i+1][j]
                            == self.board.board[i+2][j]
                            == self.board.board[i+3][j]
                            == self.board.board[i+4][j] 
                            == 1):  # human wins
                        return 1

                    elif (self.board.board[i][j] == self.board.board[i+1][j]
                            == self.board.board[i+2][j] 
                            == self.board.board[i+3][j] 
                            == self.board.board[i+4][j] 
                            == 2):  # ai wins
                        return 2

            # check diagnally from upleft to downright
            for i in range(self.bound2):
                for j in range(self.bound2):
                    if (self.board.board[i][j] == self.board.board[i+1][j+1]
                            == self.board.board[i+2][j+2]
                            == self.board.board[i+3][j+3]
                            == self.board.board[i+4][j+4]
                            == 1):  # human wins
                        return 1

                    elif (self.board.board[i][j] == self.board.board[i+1][j+1]
                            == self.board.board[i+2][j+2] 
                            == self.board.board[i+3][j+3] 
                            == self.board.board[i+4][j+4] 
                            == 2):  # ai wins
                        return 2

            # check diagnally from upright to downleft
            for i in range(self.bound2):
                for j in range(self.bound2):
                    if (self.board.board[i+4][j] == self.board.board[i+3][j+1]
                            == self.board.board[i+2][j+2]
                            == self.board.board[i+1][j+3]
                            == self.board.board[i][j+4]
                            == 1):  # human wins
                        return 1

                    elif (self.board.board[i+4][j] 
                            == self.board.board[i+3][j+1]
                            == self.board.board[i+2][j+2]
                            == self.board.board[i+1][j+3]
                            == self.board.board[i][j+4]
                            == 2):  # ai wins
                        return 2

        # if the game is a tie, return 3 and call the end game function
        else:
            return 3

    def check_occupancy(self, row, col):
        """
        Check the whether the spot is filled or not,
        and if it is human's turn, put 1, ai's turn put 2
        """
        flag = self.player_turn()
        if self.board.board[row][col] == 0 and flag: # fill the spot with one, and it's always human
            self.board.board[row][col] = 1
            self.count += 1
        elif self.board.board[row][col] == 0 and not flag:
            return
        else:
            print("Please click another spot")

    def Occupy(self, row, col, color):
        """
        Check whether this spot is occupied or not
        """
        if self.isFull(row, col):
            return
        self.board.board[row][col] = color
        self.count += 1

    def isFull(self):
        """
        Check if the board is filled with all stones
        """
        return self.count == self.size * self.size

    def player_turn(self):
        """
        If the mod is odd number, it's ai's turn, else human
        """
        if self.count % 2 == 0:
            return True
        else:
            return False

    def update(self):
        """
        Put the stone in the board
        """
        for i in range(self.board.rows):
            for j in range(self.board.cols):
                if self.board.board[i][j] == 1:
                    pos_x = (j + 0.5) * self.board.SPACING
                    pos_y = (i + 0.5) * self.board.SPACING
                    self.black = Stone(0, pos_x, pos_y)
                    self.black.display()

                elif self.board.board[i][j] == 2:
                    # write an algorithm and change the coordinate to random
                    pos_x = (j + 0.5) * self.board.SPACING
                    pos_y = (i + 0.5) * self.board.SPACING
                    self.white = Stone(255, pos_x, pos_y)
                    self.white.display()

    def end_game(self, res):
        """
        pass the result of the game from end game function
        """
        TEXT_SIZE = 70
        SPACING = 200
        
        fill(131, 250, 146)
        textSize(TEXT_SIZE)

        if res == 0:  # game still continues
            self.end = False
            # return 0
        elif res == 1:  # human wins
            self.end = True
            text("HUMAN WINS!", self.board.SIZE /
                 2 - SPACING, self.board.SIZE / 2)

        elif res == 2:  # computer wins
            self.end = True
            text("AI WINS!", self.board.SIZE /
                 2 - SPACING, self.board.SIZE / 2)

        elif res == 3:
            self.end = True
            text("IT'S A TIE!", self.board.SIZE /
                 2 - SPACING, self.board.SIZE / 2)

    def input(self, message=''):
        """
        Create the input function under JVM
        """
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def read_file(self, file_name):
        """
        Read text file and record it in a form a dictionary
        """
        MULTI = 2
        with open(file_name, 'r') as f:
            for line in f:
                # space between the name and the number 
                # and more than one user has been recorded
                user_name = line.split(" ")
                # ["sundri", "lai", "1"]  sundri lai 1
                if len(user_name) >= MULTI:
                    user_name[0] = ' '.join(user_name[:-1])  # ["sundri lai"]
                self.list_of_names[user_name[0]] = int(
                    user_name[-1])  # "1" -> 1  string to int

    def sort_winners(self, file_name):
        """
        Sort the dictionary (list_of_names) and write it back to the file
        """
        d = self.list_of_names
        d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        with open(file_name, 'w') as f:
            for item in d:
                f.write(str(item[0])+" "+str(item[1]) + '\n')

    def winner_list(self, file_name):
        """
        Read the score file and write to the file
        """
        self.read_file(file_name)  # first read the name from the txt file
        name = self.input("Enter your name: ")
        if name in self.list_of_names:
            self.list_of_names[name] += 1
        else:
            self.list_of_names[name] = 1

        # then sort the name from numerical order and write to text
        self.sort_winners(file_name)
        
    def ai_dot(self):
        """puts an ai dot in the board"""
        a = self.ai.get_random_coordinate()
        row = a[0]
        col = a[1]
        if self.board.board[row][col] == 0:
            # fill the spot with 2, that means it is ai's spot
            self.board.board[row][col] = 2
            self.count += 1

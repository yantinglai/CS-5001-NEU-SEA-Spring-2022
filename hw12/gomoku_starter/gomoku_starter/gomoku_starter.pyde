from gomoku import Gomoku
from board import Board
import time

rows = 15
cols = 15
board = [[0 for j in range(15)] for i in range(15)]
SIZE = 900
SPACING = SIZE / rows  # 60
gc = Gomoku()
board = Board()
R = 155
G = 122
B = 31


def setup():
    """Set up the canvas"""
    size(SIZE, SIZE)
    background(R, G, B)  # warm yellow wooden color


def drawBoard():
    """Draw a Gomoku board"""
    stroke(0)  # stroke color of the board line
    strokeWeight(5)  # stroke thickness of the line
    x = SPACING // 2
    y = SPACING // 2
    while x < SIZE:
        line(x, y, x, SIZE - y)  # the relations bt x and Width & Height
        x = x + SPACING

    x = SPACING // 2
    y = SPACING // 2
    while y < SIZE:
        line(x, y, SIZE - x, y)
        y = y + SPACING


def mousePressed():  # it is called every time when a mouse is pressed
    row = mouseY // SPACING
    col = mouseX // SPACING
    print("mousePress: row, col", row, col)
    gc.check_occupancy(row, col)
    gc.update()


def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)


def draw():
    drawBoard()
    if not gc.end:
        if gc.player_turn() is False:
            time.sleep(1)  # delay the movement of ai
            gc.ai_dot()
        gc.update()
        res = gc.check_winner()
        gc.end_game(res)
    else:
        gc.winner_list("score.txt")
        noLoop()  # Stop the board from drawing
        

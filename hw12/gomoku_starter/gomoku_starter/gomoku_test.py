from board import Board
from gomoku import Gomoku


def test_contructor():
    """Test the constructor"""
    gc = Gomoku()
    gc.board = Board()
    assert gc.board.rows == 15
    assert gc.board.SIZE == 900
    assert gc.board.res == 0


def test_player_turn():
    """Test the player's turn"""
    gc = Gomoku()
    gc.board = Board()
    gc.count = 0
    assert gc.player_turn() is True
    gc.count = 1
    assert gc.player_turn() is False


def test_check_occupancy():
    """Test the check_occupany"""
    gc = Gomoku()
    gc.board = Board()
    gc.board.board = [[0 for i in range(15)] for j in range(15)]
    gc.count = 0
    gc.player_turn()
    gc.check_occupancy(1, 1)
    assert gc.count == 1
    assert gc.board.board[1][1] == 1


def test_isFull():
    """Test whether the board is full"""
    gc = Gomoku()
    gc.count = 10
    gc.size = 15
    assert gc.isFull() is False
    gc.count = 225
    gc.size = 15
    assert gc.isFull() is True


def test_sort_winners():
    """Test the sort winners"""
    gc = Gomoku()
    gc.read_file("test.txt")
    gc.sort_winners("test.txt")
    with open("test.txt", 'r') as f:
        name_one = f.readline().split(" ")
        assert name_one[-1] == '5\n'
        name_two = f.readline().split(" ")
        assert name_two[-1] == '3\n'
        name_three = f.readline().split(" ")
        assert name_three[-1] == '1\n'


def test_read_file():
    """Test the read file"""
    gc = Gomoku()
    gc.read_file("test.txt")
    assert 'Sundri' in gc.list_of_names
    assert 'Bonnie' in gc.list_of_names
    assert 'Adrian' in gc.list_of_names

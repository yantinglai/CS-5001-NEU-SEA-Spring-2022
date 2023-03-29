"""starting the roll dice game"""
from game_controller import GameController


def main():

    # Create the game controller object
    gc = GameController()
    print("------------------------------")
    print("Wecome to street craps!")
    print("Rules:\nIf you roll 7 or 11 on your first roll, you win.")
    print(
        "If you roll anything else, that's your 'point', \
and you keep rolling until you either roll your point again\
 (win) or roll a 7 (lose)")

    gc.start_play()


main()

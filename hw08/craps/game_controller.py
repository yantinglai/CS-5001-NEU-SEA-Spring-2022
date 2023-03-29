"""Game controller class"""
from pair_of_dice import PairOfDice


class GameController:
    """A game controller"""
# manage rolling, scoring, and user interaction -- contains the most code

    def __init__(self):
        """Initialize the controller"""
        self.pair_of_dice = PairOfDice()

    def start_play(self):
        """Ask for user input, roll dice"""
        input("\nPress enter to roll the dice...\n")
        self.roll_dice()

    def roll_dice(self):  # die只负责
        """Roll the dice"""
        self.pair_of_dice.roll_dice()  # compare value of first roll
        self.pair_of_dice.current_value()
        res = self.pair_of_dice.sum
        self.compare_score(res)

    def roll_dice_again(self, res):
        """Roll the dice again"""
        self.pair_of_dice.roll_dice()
        self.pair_of_dice.current_value()
        new_res = self.pair_of_dice.sum

        if new_res != 7 and new_res != res:  # 这里应该是 if，我写成了while
            print(f"You rolled {new_res}")
            input("Press enter to roll the dice...")
            self.roll_dice_again(res)

        elif new_res == 7:
            print(f"You rolled {new_res}. You lose.")
            return
        elif new_res == res:
            print(f"You rolled {new_res}. You win!")
            return

    def compare_score(self, res):
        """Compare score"""
        if res == 2 or res == 3 or res == 12:
            print(f"You rolled {res}. You lose.")
            return
        elif res == 7 or res == 11:
            print(f"You rolled {res}. You win!")
            return
        else:
            print(f"Your point is {res}")
            input("Press enter to roll the dice")
            self.roll_dice_again(res)

# 问题：如何区分第一次和第二次摇色子？通过什么样的方法？我写了一个roll dice second time的method来将两者进行区分

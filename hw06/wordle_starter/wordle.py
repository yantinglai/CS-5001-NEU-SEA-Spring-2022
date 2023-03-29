""" CS5001: WORDLE GAME by YANTING LAI """
import sys
import random

G = '\x1b[0;30;42m'  # green text
Y = '\x1b[0;30;43m'  # yellow text
N = '\x1b[0m'        # normal text/no highlighting


ALLOWED_GUESSES = 6
WORD_LENGTH = 5
letter_freq = [0] * 26


# get the secret word
def get_secret():
    """
    Get secret word from user input or from file
    """
    if len(sys.argv) > 1:
        secret_word = sys.argv[1].upper()  # make it into upper case
    else:
        valid_list = get_valid_words()
        secret_word = valid_list[random.randint(0, len(valid_list)-1)].upper()
    return secret_word


# Handle uer input guess word
def format_guess(guess_word, secret_word, letter_freq):
    """
    Handle user input guess word
    """

    for char in secret_word:
        letter_freq[ord(char)-ord("A")] += 1
    formatted_guess = ""

    for i, letter in enumerate(guess_word):
        if letter_freq[ord(letter) - ord('A')] > 0:
            if letter == secret_word[i]:
                formatted_guess += G + letter
                letter_freq[ord(letter) - ord('A')] -= 1
            else:
                formatted_guess += Y + letter
        else:
            formatted_guess += N + letter
    return formatted_guess + N


# Get valid words
def get_valid_words():
    """
    Get valid words
    """
    try:
        with open('Collins Scrabble Words (2019).txt', 'r', encoding="utf-8") \
                as file:
            valid_list = []
            str_list = file.read().splitlines()
            for i in str_list:
                if len(i) == 5:
                    valid_list.append(i)
        return valid_list

    except FileNotFoundError as _:
        print("Unable to open Collins Scrabble Words (2019).txt")
        return


# Start the guess
def main():
    """
    Start the guess
    """

    secret_word = get_secret()  # 2 ways to generate secret words

    print(f"Welcome to {Y}PY{G}WOR{Y}D{G}LE{N}!")  # Welcome sentence

    full_list = []
    tries = 0

    while tries < ALLOWED_GUESSES:
        # what is an invalid input?
        # length ！= 5, a number, a character
        guess_word = input(
            f"Enter your guess ({WORD_LENGTH} letters): \n").upper()
        while (len(guess_word) != WORD_LENGTH
                or any([not x.isalpha() for x in guess_word])):
            guess_word = input(
                f"Enter your guess ({WORD_LENGTH} letters): \n").upper()
        tries += 1

        formatted_guess = format_guess(guess_word, secret_word, letter_freq)
        full_list.append(formatted_guess)
        for string in full_list:
            print("\t\t" + string)

        if guess_word == secret_word:
            print(f"Congrats You got it in {tries} tries")
            return

    print(f"Sorry, the word was {secret_word}")


main()

# 程序里面的cornercase：
# 1. 如果输入的不是五位字母，不会纳入到tries的计算当中

# Mistakes that I've made:
# 1. file.readlines() 得到的每个字符串后面有换行符/n，要使用 file.read().splitlines() 得到的才是字符串
# 2. secret_word 的值要用.upper()处理，否则在 ord(char) - ord('A') 的时候，会显示index超界
# 3. sys.argv[1]不应该在main方法里面传值，应该让main保持为空，进入get_secret之后再对sys.argv[1]进行长度判断
# 4. valid_list = get_valid_words() 要把return的value assign给一个variable
# 5. len(str_list)我赋值给了N，这个N又和老师定义的N(颜色)重复了
# 6. ord(char) - ord('A') 要注意 大写 - 大写，小写 - 小写

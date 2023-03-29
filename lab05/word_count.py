""" CS5001: Word Count by YANTING LAI """
import re


def main():
    """
    Count Words, Characters, Letters & Numbers
    str -> int
    """
    file_name = input("Please enter the file name: ")

    try:
        with open("lab05\\"+file_name, 'r', encoding="utf-8") as file:  # 中间不能有空格
            # Read File txt -> str
            new_file = file.read()

            # Calculate the number of words in the txt by split() and len()
            words = new_file.split()

            # Calculate the number of characters in the text without " " and "\n"
            no_space_file = new_file.replace(
                " ", "")  # strip the space in file
            characters = no_space_file.replace(
                "\n", "")  # strip the \n in file

            # Find all numbers and letters
            letters_and_numbers = re.findall(r'[\w\d]', new_file)
    except FileNotFoundError as _:
        print(f"Can't open {file_name}")
        return

    print("Words:", len(words))
    print("Characters:", len(characters))
    print("Letters & Numbers:", len(letters_and_numbers))


main()

# alphanumeric: a character that is either a letter or a number
# [\w\d]: \w: match all word characters, \d: match all digits

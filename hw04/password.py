""" CS5001: Username and Password Generator by YANTING LAI """
import random

print("Welcome to the username and password generator! ")

# Get input from the user
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
fav_word = input("Please enter your favourite word: ")

# Generate a random username based on the previous input
def username():
    """
    Generate username
    str -> str
    """
    first_letter = (first_name[0]).lower()
    if len(last_name) < 7:
        seven_character = last_name + (7-len(last_name))*"*"
    else:
        seven_character = last_name[6]
    num = random.randint(0,99)
    user_name = first_letter + seven_character.lower() + str(num)
    print("Thanks",first_name,", your user name is", user_name )

username()

# Show three random passwords for users
print("Here are three suggested passwords for you to consider: \n")

# Created a replace_string() method for password1
def replace_string(any_string):
    """
    Replace string letters
    str -> str
    """
    string = ""
    for i in any_string:
        if i == 'a':
            string += '@'
        elif i == 'o':
            string += '0'
        elif i == 'l':
            string += '1'
        elif i == 's':
            string += '$'
        else:
            string +=i
    return string

new_first_name = replace_string(first_name)
new_last_name = replace_string(last_name)

Password1 = new_first_name.lower() +\
                    str(random.randint(0,99))+\
                    replace_string(new_last_name.lower())
print(f"Password 1: {Password1}")

# Code block for generating passwrod2
password2 = first_name[0::-1].lower() + first_name[-1:].upper() +\
            last_name[0::-1].lower() + last_name[-1:].upper() +\
            fav_word[0::-1].lower() + fav_word[-1:].upper()

print(f"Passwrod 2: {password2}")

# Code block for generating password3
password3 = first_name[:random.randint(1,len(first_name)+1)] +\
            last_name[:random.randint(1,len(last_name)+1)] +\
            fav_word[:random.randint(1,len(fav_word)+1)]

print(f"Password 3: {password3}")

"""" CS5001: Luhn's algorithm, check validity of ID and car numbers """


def main():
    """
    Check number validity
    str -> None
    """
    acc_number = input("Please enter your credit card or your ID numbers: ")
    length = len(acc_number)
    sum = 0
    DOUBLE = 2
    TEN = 10
    for letter in acc_number[length-2::-2]:
        letter = int(letter) * DOUBLE
        first_digit = letter % TEN
        second_digit = letter // TEN
        letter = first_digit + second_digit
        sum += letter

    for letter in acc_number[length-1::-2]:
        sum += int(letter)

    if sum % TEN != 0:
        print("This number is not valid")
    elif sum % TEN == 0:
        print("This number is valid")


main()

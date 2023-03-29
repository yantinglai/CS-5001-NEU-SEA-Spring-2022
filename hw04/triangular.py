"""CS5001: Calculate the triangular number from user input BY YANTING LAI"""
import sys

def main():
    """
    Calculate the sum from 1 to n
    int -> str
    """
    input_number = int(sys.argv[1])
    res = 0
    for i in range(1,input_number+1):
        res += i
    print(f"The sum of values between 1 and {input_number} is {res}")

main()

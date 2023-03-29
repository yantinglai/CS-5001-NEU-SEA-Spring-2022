""" CS5001: Making a rocket by YANTING LAI"""
import sys


def main():
    """
    Make the entire rocket by calling the nose_cone(), fuselage(),and tail()
    List -> None
    """
    # Get parameters of height, width(number), and optional argument
    height = int(sys.argv[1])
    number = int(sys.argv[2])
    word = None

    # Check the length of the sys.argv array
    if len(sys.argv) > 3:
        word = str(sys.argv[3]).lower()
        if word != 'striped':
            word = None

    # Call functions to print out each part of the rocket
    nose_cone(height)
    fuselage(height, number, word)
    tail(height)

# Print out the nose cone


def nose_cone(height):
    """
    Make the nose cone of the rocket
    int -> None
    """

    # When the input is odd number
    if height % 2 != 0:
        row = (height+1)//2 - 1
        for i in range(0, row):
            print(" "*(row - i) + "*"*(2 * i + 1) + " "*(row - i))

    # When the input is even number
    if height % 2 == 0:
        row = height//2
        for i in range(0, row):
            print(" "*(row - i) + "*"*(2 * i) + " "*(row - i))

# Print out the fuselage


def fuselage(height, number, word):
    """
    Make the fuselage of the rocket
    int, int, str -> None
    """

    # Print rocket without striped
    while number > 0 and word is None:
        for _ in range(0, height):
            print("X" * height)
        number -= 1  # need to write it outside the while loop!

    # Print rocket with striped
    while height % 2 != 0 and number > 0 and word == "striped":
        for _ in range(0, (height+1)//2 - 1):
            print("_"*height)
        for _ in range((height+1)//2 - 1, height):
            print("X"*height)
        number -= 1

    while height % 2 == 0 and number > 0 and word == "striped":
        for _ in range(0, height//2):
            print("_"*height)
        for _ in range(height//2 + 1, height+1):
            print("X"*height)
        number -= 1

# Print the tail


def tail(height):
    """
    This is the tail function
    int -> None
    """

    if height % 2 != 0:
        mid = (height-1)//2
        for i in range(0, mid-1):
            if mid + 2*i < height:
                print(" "*((height-mid-2*i)//2) + "*" *
                      (mid + 2*i) + " "*((height-mid-2*i)//2))

        for i in range(mid-1, mid):
            print("*"*height)
            print("*"*height)

    if height % 2 == 0:
        mid = height // 2
        for i in range(0, mid-1):
            print(" "*((height - mid-2*i)//2) + "*" *
                  (mid + 2*i) + " "*((height - mid-2*i)//2))
        for i in range(mid-1, mid):
            print("*"*height)


main()

# 问题总结：
# sys.argv 的输入值要写进main方法里面
# function的呼叫也在main里面执行完毕
# 需要学习正确的代码书写格式（看文档链接）
# optional 的传入值使用的其实是一个判断的方法

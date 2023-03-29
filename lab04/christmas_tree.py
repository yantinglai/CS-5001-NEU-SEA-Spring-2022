"""This is a program to create a Christmas tree"""
def input_value():
    '''
    A function to identity whether the input is odd or even number
    '''
    number = int(input("Please enter an odd number: "))
    while number % 2 == 0:
        number = int(input("Please make sure you enter an odd number: "))
    return number

#print(type([1,2,3]))
col = input_value()
row = (col+1)//2

for i in range(1,row+1):
    for j in range(1,col+1):
        if i == 1 and j == row:
            print("*", end="")
        elif  i+j== row+1:
            print("/", end="")
        elif j-i == row-1:
            print("\\", end="")  # 注意打印特殊字符“\”反斜杠的时候，要写成'\\'的格式，否则程序会报错
        elif i == row and j!=1 and j!=col:
            print("_", end="")
        else:
            print(" ", end="")
    print()

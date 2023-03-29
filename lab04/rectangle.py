"""This is a code to print a hollow rectangle"""
symbol = input("Please any a symbol you would like to make a rectangle(eg., &, #, +, n, s, 3): ")
row = int(input("Please enter the height number of this rectangle: "))
col = int(input("Please enter the width number of this rectangle: "))

for i in range(row):
    for j in range(col):
        if i==0 or i == row-1 or j==0 or j == col-1:
            print(symbol, end=' ')
        else:
            print(" ", end=' ')
    print()

"""This is a magic square validator"""
matrix_original = []
def create_matrix(number):
    '''Go through the string and convert it to int'''
    row = []
    for i in number:
        row.append(int(i))
    return row

n1 = input("Enter a magic number:\n")
row1 = create_matrix(n1)
matrix_original.append(row1)

n2 = input()
row2 = create_matrix(n2)
matrix_original.append(row2)

n3 = input()
row3 = create_matrix(n3)
matrix_original.append(row3)

N =3

'''Check if it is magic square'''
def check_magic_square(matrix):
    '''This is the code'''
    corner_sum=0
    for i in range(0,N):
        corner_sum += matrix[i][i]
    for i in range(0,N):
        row_sum = 0
        for j in range(0,N):
            row_sum += matrix[i][j]
        if row_sum != corner_sum:
            return False

    for i in range(0,N):
        col_sum = 0
        for j in range(0,N):
            col_sum += matrix[j][i]
        if corner_sum != col_sum:
            return False
    return True

if check_magic_square(matrix_original):
    print("This is a magic square!")
else:
    print("This is not a magic square!")


# each line should consist of 3 numerical characters
# 3 rows, 3 cols, 2 corner to corner diagnoals
# Output： Not a magic square!  vs This is a magic square!

# 问题分解：
# 1. 从user那里获得三行input，并且把它储存成一个2D数组
# 2. 通过获取 index 的方式，来进行数组判定 -- 这个已经有答案
# 全局变量的命名不能够和局部变量一样！必须要对名字进行更改才可以！

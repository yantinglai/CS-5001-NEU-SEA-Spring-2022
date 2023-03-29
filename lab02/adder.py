
def main():
    number1 = int(input("Enter a first value: "))
    number2 = int(input("Enter a second value: "))
    sum = number1 + number2

    print(f"The sum of {number1} + {number2} is {sum}")

main()

# 问题：如何在adder 里面定义一个function？？？
# 遇到的错误：adder() missing 2 required positional arguments: 'num1' and 'num2' 
# 我犯的错误：input总是得到string，所以要把 input得到的string转成int！
# print 那里又忘记写 f了，问题是：什么时候要写 f，什么时候不写？真的很疑惑
from stack import Stack


class StringProcessor:
    """A string processor class"""

    def process_string(self, line):
        solution_string = ""
        stack = Stack()

        if line is None:
            return solution_string

        for letter in line:
            if letter == '*':
                solution_string += str(stack.pop())  # 此时stack里面有元素？什么时候进去的？
            elif letter == '^':
                if len(line) == 1 or len(line) == 2:  # 不加條件判斷的話 stack.pop()會為空
                    return solution_string
                solution_string += str(stack.pop())
                solution_string += str(stack.pop())
            else:
                stack.push(letter)

        return solution_string


# 如何讓输入的string 拥有 stack 的性质？不需要！直接用stack.push(letter)把 string里面的元素推入栈内即可！
# pop()功能漏了一个()
# 报错：https://stackoverflow.com/questions/42804433/what-does-this-bound-method-stack-pop-of-main-stack-object-at-0x03c74ab0
# if len(line) == 1 or len(line) == 2:  # 不加條件判斷的話 stack.pop()會為空

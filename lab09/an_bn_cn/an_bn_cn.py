from stack_python_list import Stack
import sys
sys.path.append("..")


class AnBnCn:
    """Class for evaluating strings of AnBnCn"""

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def accept(self, in_string):
        expect_a = True
        expect_b = False  # Cannot expect b until we have seen a
        expect_c = False  # Cannot expect c until we have seen b

        for char in in_string:
            if char == 'a':
                expect_b = True  # Once we have seen a, we can expect to see b
                if expect_a:
                    self.stack1.push('a')
                else:
                    return False

            elif char == 'b':
                expect_a = False  # We have seen a before
                expect_c = True   # We haven't seen c yet
                if not expect_b:  # handle case like ac
                    return False
                self.stack2.push('b')

            elif char == 'c':
                expect_a = False
                if not expect_c:
                    return False
                elif self.stack1.is_empty() or self.stack2.is_empty():
                    return False
                else:
                    self.stack1.pop()
                    self.stack2.pop()

        if self.stack1.is_empty() and self.stack2.is_empty():
            return True
        return False

    def clear(self):
        """Clear the stack at the end of each checker"""
        self.stack1 = Stack()
        self.stack2 = Stack()

# Bug that I had
# 1 Stack object is not subscriptable

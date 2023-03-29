from stack_python_list import Stack
import sys
sys.path.append("..")



class AnBnCn:  
    """Class for evaluating strings of AnBnCn"""
    def __init__(self):
        self.stack = Stack()
       

    def accept(self, in_string):
        self.new_string = in_string
        new_stack = Stack()

        expect_a = True
        expect_b = False
        expect_c = False

        for char in in_string:
            if char == 'a':
                if expect_a:
                    self.stack.push('a')
                else:
                    return False
                    
            elif char == 'b':

                expect_a = False
                expect_c = True
                self.stack.pop()
                self.stack.new_stack.push('b')
                print("pop a and push b")
        
            elif char == 'c':
                expect_a = False
                expect_b = False
                print("pop 1 b")
                self.stack.pop()

                    
        if self.stack.is_empty():
            return True
        return False
    

    def clear(self):
        """Clear the stack at the end of each checker"""
        self.stack = Stack()

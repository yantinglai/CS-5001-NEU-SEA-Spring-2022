from queue import Queue
from stack import Stack


class WordLadder:
    """A class providing functionality to create word ladders"""
    # TODO:
    # Implement whatever functionality is necessary to generate a
    # stack representing the word ladder based on the parameters
    # passed to the constructor.
    def __init__(self, w1, w2, wordlist):
        self.w1 = w1
        self.w2 = w2
        self.wordlist = wordlist

    def check_word(self, w1, w2):
        if len(w1) != len(w2):
            return None
        else:
            self.make_ladder()
    
    def make_ladder(self):
        stack = Stack()
        queue = Queue()
        word_set = set()
        alpha = "abcdefghijklmnopqrstuvwxyz"
        new_word = ""

        stack.push(self.w1)  # push w1 into the stack
        queue.enqueue(stack)  # insert stack into queue
        temp = queue.dequeue()  # dequeue the stack
        while temp:
            word = temp.peek()
            for i in range(len(self.w1)):
                for j in alpha:
                    new_word = word[:i] + j + word[i+1:] # slicing这里错写成 word[i+1:-1] 还是切片法不熟悉！
                    if new_word in self.wordlist and new_word not in word_set:
                        # print(new_word) 到 data,date,dato 就没有了
                        word_set.add(new_word)
                        new_stack = temp.copy()  # 为什么要拷贝啊
                        new_stack.push(new_word)  # 为什么要把单词放进去啊
                        if new_word == self.w2:
                            return new_stack
                        else:
                            queue.enqueue(new_stack)
                        
            if queue.isEmpty():
                return None
            else:
                temp = queue.dequeue()




                


        
        






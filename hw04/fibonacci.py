""" CS5001: Generate a list of fibonacci numbers by YANTING LAI """
import sys

def fibonacci():
    """
    Enter a value and generate a fibonacci list
    """
    sequence =[0,1]
    input_num = int(sys.argv[1])
    for _ in range(2,input_num):
        new_num = sequence[-1] + sequence[-2] # sum of the last two nbrs = the new nbr
        sequence.append(new_num)
    print(sequence)
    return sequence  # Even without a return line here, the code will be fine

fibonacci()

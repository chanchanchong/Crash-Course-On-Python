# Average Function

import math
import os
import random
import re
import sys



def avg(*nums):
    return sum(nums)/len(nums)

if __name__ == '__main__':

# Python Reverse Word and Swap Cases
    # !/bin/python

    import math
    import os
    import random
    import re
    import sys


    #
    # Complete the 'reverse_words_order_and_swap_cases' function below.
    #
    # The function is expected to return a STRING.
    # The function accepts STRING sentence as parameter.
    #

    def reverse_words_order_and_swap_cases(sentence):
        word_list = sentence.split()
        reversed_list = word_list[:: -1]
        reversed_sentence = " ".join(reversed_list)
        return reversed_sentence.swapcase()


    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        sentence = raw_input()

        result = reverse_words_order_and_swap_cases(sentence)

        fptr.write(result + '\n')

        fptr.close()

# Python Shape Classes with Area method

#!/bin/python3

import math
import os
import random
import re
import sys



class Rectangle:
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length

    pass

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    pass
if __name__ == '__main__':
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

#Manual init of array for testing local.  Commenting out for submission
#ar = []

def simpleArraySum(ar):
    #size of ar must be > 0
    # each value in ar must be <= 1000
    #sum values of ar
    
    arSum = 0

    if len(ar) > 0:
        for i in ar:
            if i >= 0 and i <= 1000:
                arSum = arSum + i
            else:
                 print(f'Array value at position {i} is out of bounds')

        print(f'Total sum of array is: {arSum}')
        return arSum

    else:
        print('Array must not be empty')
        return 0

#Method Call to test functionality. Commenting out for submission.
#simpleArraySum(ar)

#Included hacker rank code
'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
'''
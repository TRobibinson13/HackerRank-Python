#!/bin/python3

import math
import os
import random
import re
import sys

a = [1,2,3]
b = [3,2,1]

def compareTriplets(a, b):
    arSizeMax = 3
    i = 0
    aPoints = 0
    bPoints = 0
    arCompare = [0, 0]

    validateTriplet(a)
    validateTriplet(b)

    while i < arSizeMax :
        if a[i] > b[i]:
            print(f'Triplet A has been awarded +1 point for the value at position {i}')
            aPoints += 1
        elif b[i] > a[i]:
            print(f'Triplet B has been awarded +1 point for the value at {i}')
            bPoints += 1
        elif a[i] == b[i]:
            print(f'No points awarded. Triplet values at position {i} are equal.')
        
        i += 1

    arCompare = [aPoints, bPoints]
    print(f'The final scores.  Triplet A: {aPoints}.  Triplet B: {bPoints}')
    return arCompare

def validateTriplet(ar):
    for x in ar:
        if x < 1 or x > 100:
            print(f'The following tripplet has invalid parameters: {ar}')
            return 0

compareTriplets(a, b)
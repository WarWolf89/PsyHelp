import random
import sys
import os
import math

def getAbs(number):
    return math.sqrt(number*number)

try:
    number = int(sys.stdin.readline())
except ValueError:
    print("apadat")
else:
    print int(getAbs(number))







#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solution' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING s as parameter.
#

def solution(s):
    # Write your code here

    # 입력문자
    s_list = list(s)
    s_list_cnt = len(s_list)

    # 알파벳
    import string
    x1 = list(string.ascii_uppercase)
    x2 = x1[::-1]
    x1 = x1 * 26
    x2 = x2 * 26

    # value
    value = 0

    for i in range(s_list_cnt):
        value += min(x1.index(s_list[i]), x2.index(s_list[i]))
        x1 = x1[x1.index(s_list[i]):]
        x2 = x2[x2.index(s_list[i]):]

    if s_list[0] == 'Z':
        print(value + 1)
    else:
        print(value)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solution(s)

    fptr.write(str(result) + '\n')

    fptr.close()
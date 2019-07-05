"""
link:https://www.hackerrank.com/challenges/plus-minus/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&isFullScreen=false
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

For example, given the array  there are  elements, two positive, two negative and one zero. Their ratios would be ,  and . It should be printed as

0.400000
0.400000
0.200000
Function Description

Complete the plusMinus function in the editor below. It should print out the ratio of positive, negative and zero items in the array, each on a separate line rounded to six decimals.

plusMinus has the following parameter(s):

arr: an array of integers
Input Format

The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers describing an array of numbers .

Constraints



Output Format

You must print the following  lines:

A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeros in the array compared to its size.
Sample Input

6
-4 3 -9 0 4 1
Sample Output

0.500000
0.333333
0.166667
Explanation

There are  positive numbers,  negative numbers, and  zero in the array.
The proportions of occurrence are positive: , negative:  and zeros: .





"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive=len([1 for i in arr if i > 0]) / len(arr)
    negative=len([1 for i in arr if i<0])/len(arr)
    zero=len([1 for i in arr if i==0])/len( arr)

    print('{0:.6f}'.format(positive))
    print('{0:.6f}'.format(negative))
    print('{0:.6f}'.format(zero))



"""n = int(input())

arr = list(map(int, input().rstrip().split()))"""
"""arr=[-4, 3, -9 ,0 ,4, 1]
plusMinus(arr)"""



# Complete the staircase function below.
def staircase(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"#"*i)



"""
staircase(6)
"""
def miniMaxSum(arr):
    print(sum(arr)-max(arr), sum(arr)-min(arr))

miniMaxSum([7, 69, 2, 221, 8974])
"""
https://www.hackerrank.com/challenges/birthday-cake-candles/problem?h_r%5B%5D%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D%5B%5D=next-challenge&h_v%5B%5D%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D%5B%5D=zen&isFullScreen=false&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

"""
def birthdayCakeCandles(ar):
    big=max(ar)
    count=0
    for i in ar:
        if i==big:
            count+=1
    return count

def timeConversion(s):
    #
    # Write your code here.
    #
    if s[-2:]=="PM":
        if s[:2]=="12":
            return s[:-2]
        s=str(int(s[:2])+12)+s[2:-2]
        return s
    elif s[-2:]=="AM":
        if s[:2]=="12":
            s="00"+s[2:-2]
            return s
        return s[:-2]


print(timeConversion("12:45:54PM"))
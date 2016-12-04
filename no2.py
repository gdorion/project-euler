#!/bin/env python
#
#     Project Euler No2
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com

def rfib(n):
    if (n < 2):
        return 1
    r = rfib(n-1) + rfib(n-2)
    return r

def ifib(n):
    r = 0
    p1 = 1
    p2 = 2
    sum = 2

    while r <= n:
        if r % 2 == 0:
            sum = sum + r
        r = p1 + p2
        p1 = p2
        p2 = r
    return sum

print ifib(4000000)
# print ifib(21)

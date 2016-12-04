#!/bin/env python
#
#     Project Euler No3
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com

f = []
d = 2
n = 600851475143
while n > 1:
    while n % d == 0:
        f.append(d)
        n = n/d
    d = d+1
    if d^2 > n:
        if n>1:
            f.append(n)
        break
print max(f)

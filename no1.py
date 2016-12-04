#!/bin/env python
#
#     Project Euler No1
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com

sum = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum + i
print sum

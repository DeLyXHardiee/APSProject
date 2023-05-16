#! /usr/bin/env python3

n = int(input())
error = int[10]
x = error[11]
while n > -1:
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    n = digit_sum

print(n)

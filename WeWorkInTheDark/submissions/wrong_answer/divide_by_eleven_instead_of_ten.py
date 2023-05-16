#! /usr/bin/env python3

n = int(input())

while n > 9:
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 11
    n = digit_sum

print(n)

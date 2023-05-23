#! /usr/env/python3

import sys
import re

def is_between(lower_limit, number, upper_limit):
    return lower_limit <= number <= upper_limit

visited = set()
first_line = sys.stdin.readline()
assert re.match(r"(0|[1-9][0-9]*) (0|[1-9][0-9]*) (0|[1-9][0-9]*)", first_line), first_line
input_list = first_line.split(" ")
x = int(input_list[0])
y = int(input_list[1])
assert is_between(1, x, 1000)
assert is_between(1, y, 1000)
n = int(input_list[2])

for _ in range(n):
    line = sys.stdin.readline()
    line_as_list = line.split(" ")
    assert re.match(r"(0|[1-9][0-9]*) (0|[1-9][0-9]*) (0|[1-9][0-9]*)", line), line
    assert is_between(0, int(line_as_list[0]), x)
    assert is_between(0, int(line_as_list[1]), y)
    assert is_between(1, int(line_as_list[2]), 10)
    assert (int(line_as_list[0]), int(line_as_list[1])) not in visited
    visited.add((int(line_as_list[0]), int(line_as_list[1])))


num = sys.stdin.readline()
assert re.match(r"(0|[1-9][0-9]*)", num), num

for _ in range(int(num)):
    line = sys.stdin.readline()
    line_list = line.split(" ")
    assert is_between(0, int(line_list[1]), x)
    assert is_between(0, int(line_list[2]), y)
    assert re.match(r"[ker]", line_list[0]), line_list[0]
    if(line_list[0] == 'k'):
        assert len(line_list) == 3
    elif(line_list[0] == 'r'):
        assert len(line_list) == 4
        assert is_between(1, int(line_list[3]), 10)
    else:
        assert len(line_list) == 4

assert sys.stdin.readline() == ""
sys.exit(42)



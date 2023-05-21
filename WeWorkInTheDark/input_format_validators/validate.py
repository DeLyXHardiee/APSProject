#! /usr/env/python3

import sys
import re

# line = sys.stdin.readline()
# assert re.match(r"(0|[1-9][0-9]*)\n", line), line

# a = int(line)
# assert 0 <= a <= pow(10, 18)

# assert sys.stdin.readline() == ""
# sys.exit(42)

first_line = sys.stdin.readline()
input_list = first_line.split(" ")
assert len(input_list) == 3
for element in input_list:
        assert re.match(r"(0|[1-9][0-9]*)", element), element
# n = int(input_list[2])

""" 
for _ in range(n):
    line = sys.stdin.readline()
    line_list = line.split(" ")
    assert len(line_list) == 3
    for element in line_list:
        assert re.match(r"(0|[1-9][0-9]*)", element), element """

""" num = sys.stdin.readline()
assert re.match(r"(0|[1-9][0-9]*)", num), num

for _ in range(int(num)):
    line = sys.stdin.readline()
    line_list = line.split(" ")
    assert re.match(r"[ker]", line_list[0]), line_list[0]
    if(line_list[0] == 'k'):
        assert len(line_list) == 3
    else:
        assert len(line_list) == 4

assert sys.stdin.readline() == "" """
sys.exit(42)



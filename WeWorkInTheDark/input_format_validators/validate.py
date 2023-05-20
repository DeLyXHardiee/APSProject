#! /usr/env/python3

import sys
import re

# line = sys.stdin.readline()
# assert re.match(r"(0|[1-9][0-9]*)\n", line), line

# a = int(line)
# assert 0 <= a <= pow(10, 18)

# assert sys.stdin.readline() == ""
# sys.exit(42)

output_lines = sys.stdin.readlines()

for line in output_lines:
    assert re.match(r"(0|[1-9][0-9]*)\n", line), line.strip()
    a = int(line)
    assert 0 <= a <= pow(10, 18)

sys.exit(42)



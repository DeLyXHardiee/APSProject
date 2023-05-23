#! /usr/env/python3

import random
import sys

# (X, Y, N, M, Q)

# Generate explicit input
X = int(sys.argv[1])
Y = int(sys.argv[2])
N = int(sys.argv[3])
visited = set()
guards = []
for _ in range(N):
    x = random.randint(0, X - 1)
    y = random.randint(0, Y - 1)
    while (x,y) in visited:
        x = random.randint(0, X - 1)
        y = random.randint(0, Y - 1)
    num_guards = 10
    update = f"{x} {y} {num_guards}"
    visited.add((x,y))
    guards.append(update)

M = int(sys.argv[4])
queries = []
for _ in range(M):
    if int(sys.argv[5]) == 0:
        query_type = "e"
    else:
        query_type = random.choice(["e", "r", "k"])
    
    if query_type == "k":
        x = random.randint(0, X - 1)
        y = random.randint(0, Y - 1)
        query = f"{query_type} {x} {y}"
    elif query_type == "e":
        x = random.randint(0, X - 1)
        y = random.randint(0, Y - 1)
        r = random.randint(1, 1000)
        query = f"{query_type} {x} {y} {r}"
    else:  # Reinforcements
        x = random.randint(0, X - 1)
        y = random.randint(0, Y - 1)
        n = random.randint(1, 10)
        query = f"{query_type} {x} {y} {n}"
    queries.append(query)

# Print explicit input
print(f"{X} {Y} {N}")
for guard in guards:
    print(guard)
print(M)
for query in queries:
    print(query)
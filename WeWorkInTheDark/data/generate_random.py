import random

# Generate random input
X = random.randint(10, 1000)
Y = random.randint(10, 1000)
N = min(random.randint(100, 100000), X * Y)
visited = set()
guards = []
for _ in range(N):
    x = random.randint(0, X - 1)
    y = random.randint(0, Y - 1)
    while (x,y) in visited:
        x = random.randint(0, X - 1)
        y = random.randint(0, Y - 1)
    num_guards = random.randint(1, 10)
    update = f"{x} {y} {num_guards}"
    visited.add((x,y))
    guards.append(update)

M = random.randint(100, 100000)
queries = []
for _ in range(M):
    query_type = random.choice(["e", "r", "k"])
    if query_type == "k":
        x = random.randint(0, X - 1)
        y = random.randint(0, Y - 1)
        query = f"{query_type} {x} {y}"
    elif query_type == "e":
        x = random.randint(0, X - 1)
        y = random.randint(0, Y - 1)
        r = random.randint(1, max(X, Y))
        query = f"{query_type} {x} {y} {r}"
    else:  # Reinforcements
        x = random.randint(0, X - 1)
        y = random.randint(0, Y - 1)
        n = random.randint(1, 10)
        query = f"{query_type} {x} {y} {n}"
    queries.append(query)

#Print generated input
print(f"{X} {Y} {N}")
for guard in guards:
    print(guard)
print(M)
for query in queries:
    print(query)

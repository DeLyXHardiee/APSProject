import random
import sys

random.seed(int(sys.argv[-1])) # fix seed of random generator to last argument

#print(random.randrange(0, pow(10, 18)))

# Generate random input
X = random.randint(1, 1000000)
Y = random.randint(1, 1000000)
N = random.randint(1, min(X * Y, 100))
guards = []
for _ in range(N):
    x = random.randint(0, X - 1)
    y = random.randint(0, Y - 1)
    num_guards = random.randint(1, 10)
    query = f"{x} {y} {num_guards}"
    guards.append((x, y, num_guards))

M = random.randint(1, 1000000)
queries = []
for _ in range(M):
    query_type = random.choice(["Kill", "EagleVision", "Reinforcements"])
    if query_type == "Kill":
        x = random.randint(0, X - 1)
        y = random.randint(0, Y - 1)
        query = f"Kill {x} {y}"
    elif query_type == "EagleVision":
        x = random.randint(0, X - 1)
        y = random.randint(0, Y - 1)
        r = random.randint(1, min(X, Y))
        query = f"EagleVision {x} {y} {r}"
    else:  # Reinforcements
        x = random.randint(0, X - 1)
        y = random.randint(0, Y - 1)
        n = random.randint(1, 10)
        query = f"Reinforcements {x} {y} {n}"
    queries.append(query)

# Print generated input
print(f"{X} {Y} {N}")
for guard in guards:
    print(f"{guard[0]} {guard[1]} {guard[2]}")
print(M)
for query in queries:
    print(query)
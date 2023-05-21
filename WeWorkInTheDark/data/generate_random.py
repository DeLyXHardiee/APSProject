import random
import sys

#random.seed(int(sys.argv[-1])) # fix seed of random generator to last argument

#print(random.randrange(0, pow(10, 18)))

# Generate random input
X = random.randint(10, 1000)
Y = random.randint(10, 1000)
N = random.randint(100, 100000)
guards = []
for _ in range(N):
    x = random.randint(0, X - 1)
    y = random.randint(0, Y - 1)
    num_guards = random.randint(1, 10)
    update = f"{x} {y} {num_guards}"
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

# Print generated input
print(f"{X} {Y} {N}")
for guard in guards:
    print(guard)
print(M)
for query in queries:
    print(query)

# filename = "input.txt"  # Change the filename as desired
# with open(filename, "w") as file:
#     file.write(f"{X} {Y} {N}\n")
#     for guard in guards:
#         file.write(f"{guard}\n")
#     file.write(f"{M}\n")
#     for query in queries:
#         file.write(f"{query}\n")
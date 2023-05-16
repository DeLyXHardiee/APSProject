import random
import sys

random.seed(int(sys.argv[-1])) # fix seed of random generator to last argument


print(random.randrange(0, pow(10, 18)))

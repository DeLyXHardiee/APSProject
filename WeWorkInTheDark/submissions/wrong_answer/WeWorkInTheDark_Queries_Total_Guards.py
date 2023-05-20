class FenwickTree2D:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.tree = [[0] * (m + 2) for _ in range(n + 2)]

    def update(self, x, y, val):
        i = x + 1
        while i <= self.n:
            j = y + 1
            while j <= self.m:
                self.tree[i][j] += val
                j += j & -j
            i += i & -i

    def query(self, x, y):
        total_guards = 0
        i = x + 1
        while i > 0:
            j = y + 1
            while j > 0:
                total_guards += self.tree[i][j]
                j -= j & -j
            i -= i & -i
        return total_guards

def main():
    input_str = input()
    input_list = input_str.split(" ")
    x = int(input_list[0])
    y = int(input_list[1])
    fenwick2d = FenwickTree2D(x, y)
    n = int(input_list[2])

    for _ in range(n):
        guards = input().split(" ")
        fenwick2d.update(int(guards[0]), int(guards[1]), int(guards[2]))

    m = int(input().strip())

    for _ in range(m):
        query = input().split(" ")
        command = query[0]

        if command == "eaglevision":
            ezio_range = int(query[3])
            x_lower_bound = max(0, int(query[1]) - ezio_range)
            y_lower_bound = max(0, int(query[2]) - ezio_range)
            x_upper_bound = min(x, int(query[1]) + ezio_range)
            y_upper_bound = min(y, int(query[2]) + ezio_range)
            print(
                fenwick2d.queryRange(
                    x_lower_bound, y_lower_bound, x_upper_bound, y_upper_bound
                )
            )

        elif command == "reinforcements":
            fenwick2d.update(int(query[1]), int(query[2]), int(query[3]))

        elif command == "kill":
            fenwick2d.setToZero(int(query[1]), int(query[2]))

if __name__ == "__main__":
    main()

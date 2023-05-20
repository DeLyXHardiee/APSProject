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
        sum = 0
        i = x + 1
        while i > 0:
            j = y + 1
            while j > 0:
                sum += self.tree[i][j]
                j -= j & -j
            i -= i & -i
        return sum

    def queryRange(self, x1, y1, x2, y2):
        return (
            self.query(x2, y2)
            - self.query(x1 - 1, y2)
            - self.query(x2, y1 - 1)
            + self.query(x1 - 1, y1 - 1)
        )

    def setToZero(self, x, y):
        value = (
            self.query(x, y)
            - self.query(x - 1, y)
            - self.query(x, y - 1)
            + self.query(x - 1, y - 1)
        )
        self.update(x, y, -value)
        
def main():
    input_str = input()
    input_list = input_str.split(" ")
    x = int(input_list[0])
    y = int(input_list[1])
    fenwick2d = FenwickTree2D(x, y)
    n = int(input_list[2])

    for _ in range(n):
        guards = input().split(" ")
        guards_x = int(guards[0])
        guards_y = int(guards[1])
        guards_amount = int(guards[2])
        fenwick2d.update(guards_x, guards_y, guards_amount)

    m = int(input().strip())

    for _ in range(m):
        query = input().split(" ")
        command = query[0]

        if command == "eaglevision":
            ezio_x = int(query[1])
            ezio_y = int(query[2])
            ezio_range = int(query[3])
            x_lower_bound = max(0, ezio_x - ezio_range)
            y_lower_bound = max(0, ezio_y - ezio_range)
            x_upper_bound = min(x, ezio_x + ezio_range)
            y_upper_bound = min(y, ezio_y + ezio_range)
            print(
                fenwick2d.queryRange(
                    x_lower_bound, y_lower_bound, x_upper_bound, y_upper_bound
                )
            )

        elif command == "reinforcements":
            r_x = int(query[1])
            r_y = int(query[2])
            r_amount = int(query[3])
            fenwick2d.update(r_x, r_y, r_amount)

        elif command == "kill":
            k_x = int(query[1])
            k_y = int(query[2])
            fenwick2d.setToZero(k_x, k_y)


if __name__ == "__main__":
    main()

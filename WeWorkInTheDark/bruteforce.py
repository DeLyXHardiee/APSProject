def main():
    input_str = input()
    input_list = input_str.split(" ")
    x = int(input_list[0])
    y = int(input_list[1])
    area = [x][y]
    n = int(input_list[2])

    for _ in range(n):
        guards = input().split(" ")
        guards_x = int(guards[0])
        guards_y = int(guards[1])
        guards_amount = int(guards[2])
        area[guards_x][guards_y] = guards_amount

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
            amount = 0
            for i in range(x_lower_bound, x_upper_bound):
                for j in range(y_lower_bound, y_upper_bound):
                    amount += area[i][j]
            print(amount)

        elif command == "reinforcements":
            r_x = int(query[1])
            r_y = int(query[2])
            r_amount = int(query[3])
            area[r_x][r_y] = r_amount

        elif command == "kill":
            k_x = int(query[1])
            k_y = int(query[2])
            area[k_x][k_y] = 0


if __name__ == "__main__":
    main()

n = int(input("Enter Number: "))
matrix = [[0 for i in range(n)] for j in range(n)]


def main():
    for j in range(n):
        for i in range(n):
            if (i+j) % 2 != 0:
                matrix[i][j] = 1
            print(matrix[i][j], end="  ")
        print()


if __name__ == '__main__':
    main()

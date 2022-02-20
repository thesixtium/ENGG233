import random

def merge(a, b):
    indexA = 0
    indexB = 0
    matrix = []

    while len(matrix) != (len(a) + len(b)):
        if indexA == len(a):
            for i in b[indexB:]:
                matrix += [b[indexB]]
                indexB += 1

        elif indexB == len(b):
            for i in a[indexA:]:
                matrix += [a[indexA]]
                indexA += 1

        else:
            if a[indexA] < b[indexB]:
                matrix += [a[indexA]]
                indexA += 1
            else:
                matrix += [b[indexB]]
                indexB += 1

    return matrix

def main():
    n = 5
    m = 8

    matrixN = [random.randint(0, 50) for i in range(n)]
    matrixM = [random.randint(0, 50) for i in range(m)]

    matrixN.sort()
    matrixM.sort()

    print(matrixN)
    print(matrixM)
    print(merge(matrixN, matrixM))

if __name__ == '__main__':
    main()
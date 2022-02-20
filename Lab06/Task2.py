def cols(x):
    y = "A"
    while y <= x:
        print(y,end="")
        i = ord(y[0]) + 1
        y = chr(i)
    print("\n")

def rows(s):
    while s >= "A":
        cols(s)
        i = ord(s[0]) - 1
        s = chr(i)

def main():
    start = "I"
    rows(start)

if __name__ == '__main__':
    main()
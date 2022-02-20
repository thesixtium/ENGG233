def f2 (k):
    # Point 1
    print("Point 1")
    print("k = " + str(k))
    return k+1

def f1 (x):
    print("x = " + str(x))
    y = f2(x+1)
    print("y = " + str(y))
    y = f2(y+2)
    print("y = " + str(y))
    return y

def main():
    a = 12
    print("a = " + str(a))
    a = f1(a+1)
    print("a = " + str(a))
    print("Point 2")
    # point 2

if __name__ == "__main__":
 main()

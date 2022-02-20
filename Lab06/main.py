def f2 (k):
 # Point 1
 print("K", k)
 return k+1

def f1 (x):
 y = f2(x+1)
 print("X", x)
 print("Y", y)
 y = f2(y+2)
 return y

def main():
 a = 12
 a = f1(a+1)
 # point 2
 print("A", a)

if __name__ == "__main__":
 main()

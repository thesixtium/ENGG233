a=10

def bar(d):
    c=d+10
#--------------------------------------point3
    print("Point 3")
    print(a)
    print("No B")
    print(c)
    print(d)
    print()

    return c

def foo(a,b):
    a-=1
    b+=1
    a+=bar(b)
#--------------------------------------point2
    print("Point 2")
    print(a)
    print(b)
    print("No C")
    print("No D")
    print()

    return a+b

def main():
    b=18
    c=2
#--------------------------------------point1
    print("Point 1")
    print(a)
    print(b)
    print(c)
    print("No D")
    print()


    d=foo(b,c)
#--------------------------------------point4
    print("Point 4")
    print(a)
    print(b)
    print(c)
    print(d)
    print()

if __name__=="__main__":
    main()
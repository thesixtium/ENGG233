import random

def smaller_of_two(a,b):
    if a < b:
        return a
    else:
        return b

def greater_of_two(a,b):
    if a > b:
        return a
    else:
        return b

def is_different(x,y,z):
    if x == y == z:
        return False
    else:
        return True

def print_result(max, min):
    print("Max and Min are: ", min, max)

def min_of_three(x,y,z):
    if smaller_of_two(x, y) == smaller_of_two(x, z):
        return x
    elif smaller_of_two(x, y) == smaller_of_two(y, z):
        return y
    else:
        return z


def max_of_three(x,y,z):
    if greater_of_two(x, y) == greater_of_two(x, z):
        return x
    elif greater_of_two(x, y) == greater_of_two(y, z):
        return y
    else:
        return z

def main():
    counter = 0

    while counter < 10:
        x = random.random()
        y = random.uniform(1,100)
        z = random.randint(1,100)
        print("The three random numbers generated are: ", x, y, z)
        if (is_different(x, y, z)):
            print_result(min_of_three(x, y, z), max_of_three(x, y, z))
        else:
            print("The three numbers are the same ")

        counter += 1

if __name__ == '__main__':
    main()
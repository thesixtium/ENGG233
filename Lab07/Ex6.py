a = [3, 5, 4, 20, 10]

def duplicates(array):
    seen = []
    for i in array:
        for j in seen:
            if i == j:
                return False
        seen.append(i)
    return True

def main():
    print("Unique:", duplicates(a))

if __name__ == '__main__':
    main()
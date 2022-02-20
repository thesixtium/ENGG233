while True:
    try:
        r = int(input("Rows (Between 1 and 15): "))
        if 0 < r < 16:
            break
        else:
            print("Number is not between 1 and 15... ", end="")
    except:
        print("Not a valid number... ", end="")

while True:
    try:
        c = int(input("Columns (Between 1 and 15): "))
        if 0 < c < 16:
            break
        else:
            print("Number is not between 1 and 15... ", end="")
    except:
        print("Not a valid number... ", end="")



print("X".rjust(4), end=" ")
for j in range(1, c+1):
    print(str(j).rjust(4), end=" ")
print()
print()

for i in range(1, r+1):
    print(str(i).rjust(4), end=" ")
    for j in range(1, c+1):
        print(str(i*j).rjust(4), end=" ")
    print()
    print()
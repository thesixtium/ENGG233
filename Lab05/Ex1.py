n, count = 0, 0
sequence = [0, 1]

while True:
    n = input("Number Greater Than Three: ")
    try:
        if int(n) > 3:
            break
        else:print("Number is not greater than three... ", end="")
    except:
        print("Not a valid number... ", end="")

while int(n) > (sequence[-1] - 1):
    sequence.append(sequence[count] + sequence[count + 1])
    count += 1


print(sequence[1:-1])
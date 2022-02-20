counter = 0
sum = 0
oddNumbs = 0

userNumber = int(input("Your number: "))

while counter != userNumber:
    if counter % 2 != 0:
        print(counter)
        sum += counter
        oddNumbs += 1
    counter += 1

print("Sum is: " + str(sum))
print("Average is: " + str(sum/oddNumbs))

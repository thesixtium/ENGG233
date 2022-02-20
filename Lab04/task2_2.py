number = int(input("Enter a positive number: "))
sum = 0


while True:
    if number >= 0:
        break
    else:
        number = int(input("Invalid, number is negative. Enter a positive number: "))

while (number > 0):
    if sum != 0:
        print(" + ", end="")
    sum += number%10
    print(str(number%10), end="")
    number = number // 10


print(", which is " + str(sum))

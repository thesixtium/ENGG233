digits = input("Your six digits: ")

for i in range(len(digits)):
    if i == 0:
        print("First Number: " + digits[i])
    else:
        if( int(digits[i])%int(digits[0]) == 0):
            print(digits[i] + " is divisible by " + digits[0])

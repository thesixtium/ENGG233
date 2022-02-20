mortgageType = input("Mortgage Type: ")
mortgageTerm = input("Mortgage Term: ")

if mortgageType == "Open":
    if mortgageTerm == "one year":
        print("7.10%")
    elif mortgageTerm == "three years":
        print("7.50%")
    else:
        print("Not Available")
else:
    if mortgageTerm == "one year":
        print("5.30%")
    elif mortgageTerm == "three years":
        print("5.00%")
    else:
        print("5.75%")

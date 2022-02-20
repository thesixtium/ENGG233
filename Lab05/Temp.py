results = ""

for i in range(15):
    for j in range(i):
        results += " "
    results += "0"
    for j in range(7 - i):
        results += "*"
    for j in range(6 - i):
        results += "*"
    if i < 7:
        results += "0"
    for j in range(i):
        if i < 8:
            results += "*"
    for j in range(14 - i):
        if i > 7:
            results += "*"
    results += "\n"

print(results)
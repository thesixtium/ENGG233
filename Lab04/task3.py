foo = "ACE"
x = 0
j = 4
ch = 'a'

print("Point 1")
print("foo: " + foo)
print("x: " + str(x))
print("j: " + str(j))
print("ch: " + ch)
print()

while True:
    x = ord(ch) - ord('A')
    ch = chr(ord(ch) + 1)
    j -= 1

    print("Point 2")
    print("foo: " + foo)
    print("x: " + str(x))
    print("j: " + str(j))
    print("ch: " + ch)
    print()

    if j < 0:
        break

j += 1
y = foo[j]
print("Point 3")
print("foo: " + foo)
print("x: " + str(x))
print("j: " + str(j))
print("ch: " + ch)
print("y: " + y)


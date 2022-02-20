a = [6, 8, 18, 49]
n = 2
b = [55, 66, 77, 88]
d = [0 for x in range(11)]
d[n-1] = 100
#---Point 1


j = 4
for i in range(0, 4):
    d[i] = a[i]
    d[j] = b[i]
    j += 1
    #---Point 2


for j in range(len(d)-1, 1, -1):
    for i in range(0, j):
        tmp = d[i]
        d[i] = d[j]
        d[j] = tmp
        #---Point 3


#---Point 4
print("Point 4")
d[11] = 300*2
print("d[11]:", d[11])
a = 1
b = 1
c = 1
value = 0
fiblist = []
while c < 4000000:
    c = a + b
    a = b
    b = c
    #print(a +", ")
    fiblist.append(a)

print(fiblist)
print("length of an array = ", len(fiblist))
for i in range(0, len(fiblist)):
    if fiblist[i] % 2 ==0:
        #print(fiblist[i])
        value = value + fiblist[i]

print(value)

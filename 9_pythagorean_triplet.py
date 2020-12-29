# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

a = 1
b = 2
c = 3
for a in range(199, 202):
    for b in range(370, 376):
        for c in range(420, 426):
            if (c > b) and (b > a):
                #print("a = ", a, "b = ", b, "c = ", c)
                if (a * a) + (b * b) == (c * c):
                    if (a + b + c) == 1000:
                        print("Actually required numbers a = ", a, "b = ", b, "c = ", c)
                        print("Product of a, b, c is = ", a*b*c)
                        break
                    #print("a = ", a, "b = ", b, "c = ", c)
                    break


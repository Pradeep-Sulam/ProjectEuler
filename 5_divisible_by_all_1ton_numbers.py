# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

n = int(input("Enter the number = "))
counter = 0
i = 12252240
while (counter != n) & i < 2525:
    for j in range(1, n+1):
        if i % j == 0:
            counter = counter + 1
            # print("i value ", i, "counter ", counter, "j value ", j, "i%j", i % j)
    if counter == n:
        # print("Value = ", n, "counter = ", counter)
        print(i)
        break
    i = i + 1
    counter = 0

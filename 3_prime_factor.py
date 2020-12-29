n = int(input("Enter the number to know the prime factor's : "))
i = 1
prime_factors = []
while n > 1:
    if n % i == 0:
        #print(i)
        prime_factors.append(i)
        n = n / i
    i = i+1
print(prime_factors)
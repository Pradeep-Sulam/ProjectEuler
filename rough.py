# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# This function is used to find the given number is prime number or not.
def prime_number(n):
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter = counter + 1
    if counter == 2:
        return True
    else:
        return False


n = int(input("Enter the which prime number is required : "))
j = 1
prime_numbers_list = []
while j < 1000:
    if prime_number(j):
        prime_numbers_list.append(j)

print(prime_numbers_list[n])

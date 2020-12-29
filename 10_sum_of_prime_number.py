# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

number = int(input("Enter the number "))
n = 1
prime_number_list = []
final_value = 0
while n < number:
    counter = 0
    for i in range(1, n+1):
        if n % i == 0:
            counter = counter + 1
    if counter == 2:
        prime_number_list.append(n)
        final_value = final_value + n
    n = n + 1

print(prime_number_list)
print("sum of first prime number below", n, "is ", final_value)

number = int(input("Enter the number "))
n = 1
prime_number_list = []
while len(prime_number_list) < number:
    counter = 0
    for i in range(1, n+1):
        if n % i == 0:
            counter = counter + 1
    if counter == 2:
        prime_number_list.append(n)
    n = n + 1


print("Length - ", len(prime_number_list))
print(prime_number_list)
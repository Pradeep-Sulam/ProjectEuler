def even_number(n):
    return n//2


def odd_number(n):
    return (3 * n) + 1


def largest_number_in_list(n):
    large_number = 0
    for i in range(0, len(n)):
        if n[i] > large_number:
            large_number = n[i]
    return large_number


def collatz_counter(n):
    counter = 1
    while n > 1:
        if n % 2 == 0:
            n = even_number(n)
        else:
            n = odd_number(n)
        counter = counter + 1

    return counter


def main():
    number = int(input("Enter the number : "))
    collatz_sequence_list = []
    for i in range(1, number+1):
        collatz_sequence_list.append(collatz_counter(i))
    print(collatz_sequence_list)
    print(collatz_sequence_list.index(largest_number_in_list(collatz_sequence_list)))

main()
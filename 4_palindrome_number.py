# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome_number(actual_number):
    n = actual_number
    new_number = 0
    tmp = 0
    while n > 1:
        tmp = n % 10
        n = n // 10
        new_number = new_number * 10 + tmp

    if new_number == actual_number:
        return True
    else:
        return False


def largest_number_in_list(n):
    large_number = 0
    for i in range(0, len(n)):
        if n[i] > large_number:
            large_number = n[i]
    return large_number


def main():
    number = 0
    list_of_palindrome_number = []
    for i in range(9999, 999, -1):
        for j in range(9999, 999, -1):
            number = i * j
            if palindrome_number(number):
                list_of_palindrome_number.append(number)
    print(largest_number_in_list(list_of_palindrome_number))


main()
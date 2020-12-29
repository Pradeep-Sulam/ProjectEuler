# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# Number is placed in the text1.txt file.
f = open("text1.txt", "r+")
context = f.read()
x = context.split()
new_list = []
n = 0
sum = 0
for i in range(0, len(x)):
    n = int(x[i])
    sum = sum + n

print(sum)
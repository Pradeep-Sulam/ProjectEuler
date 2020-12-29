f = open("text.txt", "r")
content = f.read()
x = content.split()
value = 1
final_list = []
for i in range(0, len(x)):
    # left to right
    if i%20 < 17:
        value = int(x[i])*int(x[i+1])*int(x[i+2])*int(x[i+3])
        final_list.append(value)
    # Top to bottom
    if i//20 < 17:
        value = int(x[i])*int(x[i+20])*int(x[i+40])*int(x[i+60])
        final_list.append(value)

for i in range(0, len(x)-63):
    # diagonally
    if i%20 < 17:
        value = int(x[i])*int(x[i+21])*int(x[i+42])*int(x[i+63])
        final_list.append(value)
    # Reverse diagonally
    if i%20 < 17:
        value = int(x[i+3])*int(x[i+22])*int(x[i+41])*int(x[i+60])
        final_list.append(value)


def largest_number_in_list(n):
    large_number = 0
    for i in range(0, len(n)):
        if n[i] > large_number:
            large_number = n[i]
    return large_number

print(len(final_list))
print(largest_number_in_list(final_list))
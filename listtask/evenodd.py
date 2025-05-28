# Find the odd number in another list
no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for i in no:
    if i % 2 == 1:
        b.append(i)
    elif i % 2 == 0:
        b.append(i)
print(b)


numbers = (1, 2, 3, 4)
updated_numbers = []
for num in numbers:
    if num % 2 != 0:
        updated_numbers.append(num + 10)
    else:
        updated_numbers.append(num)
a = tuple(updated_numbers)
print(a)

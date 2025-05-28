numbers = [0, 1, 2, 0, 3, 0, 4]
filtered = []

for num in numbers:
    if num != 0:
        filtered.append(num)

print("List without zeros:", filtered)

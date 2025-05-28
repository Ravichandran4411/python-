st = ['a', 3, 'b', 'hello', 5, '@', '!', 'z', 'World', 9]
alphabets = []

for item in st:
    if type(item) == str and item.isalpha():
        alphabets.append(item)

print("Alphabets:", alphabets)

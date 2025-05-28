st = ('udhaiyamaran',23,23.56,'a',"true")
alphabets = []

for item in st:
    if type(item) == str and item.isalpha():
        alphabets.append(item)
a=tuple(alphabets)        
print("Alphabets:", a)

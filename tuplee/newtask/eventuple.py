no = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = []
for i in no:
    if i % 2 == 0:
        b.append(i)
a=tuple(b)        
print(a)

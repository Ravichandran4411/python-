replace_zero = (-12, 3, 4,-3,-5,-86,53,-65)
replace = []
for i in replace_zero:
    if i < 0:
        replace.append(0)
    else:
        replace.append(i)
a = tuple(replace)
print("Negatives replaced with 0:", a)

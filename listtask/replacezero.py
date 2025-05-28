
replace_zero = [-12, 3, 4, -5, -6, -7, 80, -80]
replace = []
for i in replace_zero:
    if i < 0:
        replace.append(0)
    else:
        replace.append(i)
print("Negatives replaced with 0:", replace_zero)


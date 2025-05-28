tuple = (1, 34, 60, -35, -29, 56, -46)
positive = 0
negative = 0
for i in tuple:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
print("Positive numbers:", positive)
print("Negative numbers:", negative)

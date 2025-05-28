numbers = (10,20,3,4,5,2,24,44,54,35)
total = 0
count = 0
for num in numbers:
    total += num
    count += 1
if count == 0:
    print("empty")
else:
    average = total / count
    print(average)


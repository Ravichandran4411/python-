numbers = [10, 20, 30, 40, 50, 200,234,432,546,35,]
total = 0
count = 0
for num in numbers:
    total += num
    count += 1
if count == 0:
    print("List is empty.")
else:
    average = total / count
    print("Average no is:", average)


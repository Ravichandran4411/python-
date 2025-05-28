#sum all the no in list
from functools import reduce
def add(x, y):
    return x + y
num = [1,2,3,4,5,6,7,8,9]
t = reduce(add, num)
print(t)

#multiply all the number in a list
from functools import reduce
def multiply(x, y):
    return x * y
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
t = reduce(multiply, num)
print(t)

#maximum number

number = [3, 7, 2, 9, 5, 11, 4, 78 , 700 , 567]
max = reduce(lambda x, y: x if x > y else y, number)
print(max)

#concatenate 

words = ["ravi", " ", "mani", "!", " kavin", "gd", " abi."]

result = reduce(lambda x, y: x + y, words)

print(result)


#digit all the number 
def digit(x, y):
    return x * 10 + y
digits = [1, 2, 3, 4, 44  ,5 ,6 ,7 ,8 , 10]
number = reduce(digit, digits)
print(number)
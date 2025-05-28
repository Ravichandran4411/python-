

'''#square the number

def sq(l):
    return l*l
n=[4,5,6,7,8,9]
a=map(sq,n)
print(list(a))
sq(2)'''

# #CONVERT STRING INTO UPPERCASER()
# def up(r):
#     return r.upper()
# m = ["Ravichandran","ravi"]
# b = map(up, m)
# print(list(b))

# #STRING INTO INTEGER
# string_numbers = ['1', '2', '3', '4']
# int_numbers = list(map(int, string_numbers))
# print(int_numbers)


# # Add two lists element-wise using lambda.
# def llambda():
#     list1 = [1, 2, 3, 4]
#     list2 = [10, 20, 30, 40]
#     result = list(map(lambda x, y: x + y, list1, list2))
#     print("sum:", result)

# llambda()


# #  Get the length of each string
# def lengths(strings):
#     lengths = []
#     for s in strings:
#         lengths.append(len(s))
#     return lengths


# w = ["maran","guru"]
# lengthss = lengths(w)
# print("Word:", w)
# print("Length:", lengthss)

# # check if elements are even using lambda
# number = [1, 2, 3, 4, 5, 6]
# even = list(map(lambda x: x % 2 == 0, number))
# print(even)

# #capitalize()
# w = ["ravi","kavi"]
# capitalized = list(map(lambda w: w.title(), w))
# print(capitalized)

# reverse a string
word = ["shivesh","yash","aashi"]
reverse = list(map(lambda w: w[::-1], word))
print(reverse)

# create a set 1 to 5 and add 6 to it
creset = {1, 2, 3, 4, 5}
creset.add(6)
print(creset)

# reemove number 3 from the set
set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)

#discard() and remove()
set2 = {2, 4, 6, 8, 10,7,8,9}
set2.remove(6)
print(set2)
set2.discard(4)
print(set2)

# create a set string and print
sety = {"Udhaiyamaran"}
print(sety)

# check if a number 4 exists in a set
sety = {1, 2, 3, 4, 5, 6}
print(4 in sety)

# find the union of two set
sett = {1, 2, 3, 4, 5, 6, 7}
sety = {3, 5, 2, 6, 79, 80}
set3 = sett.union(sety)
print(set3)

# intersections of two set
set1 = {1, 2, 3, 4, 5, 6,7,8,9,10,11,12}
set2 = {7, 8, 9, 10, 3, 4, 5, 6}
set3 = set1.intersection(set2)
print(set3)

# diffrence between two sets
set4= {"ravi","guru","maran"}
set5= {"maran","kavin","shivesh"}
set6=set4.difference(set5)
print(set6)

# symmentric diffrence
set7= {"a","b","c","d"}
set8= {"d","e","f","g"}
set9= set7.symmetric_difference(set8)
print(set9)


# using some operators
seta= {10, 20, 30}
setb = {24, 60, 44}
print(seta| setb)
print(seta & setb)
print(seta - setb)
print(seta ^ setb)

# removes viall duplicates from the set
listt= [10,20,20,30,50,60,70,80,90]
u = set(listt)
print(u)

# two list and common elements
list1 = [10,3,30,40,50,60,70,80]
list2 = [30,40,0,60]
c = set(list1) & set(list2)
print(list(c))


# GET UNIQUE VALUES
lis = ["apple", "banana", "apple", "orange", "banana"]
u = set(lis)
print(u)

# lengthr
r= "hello world"
u = set(r)
count = len(u)
print(count)

# square
start = 1
end = 10
square_numbers = set()
for number in range(start, end + 1):
    square = number ** 2
    square_numbers.add(square)
print(square_numbers)

# vowel
char_set = {'w', 'r', 'i', 't', 'e', 'a', 'p', 'o', 'g', 'm', 'f', 'n', 'd', 'l', 's'}
vowels = {'a', 'e', 'i', 'o', 'u'}
found_vowels = char_set.intersection(vowels)
print(found_vowels)


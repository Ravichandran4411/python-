mytuple=('ravi','maran','guru')
print(type(mytuple))
print(len(mytuple))
print(mytuple[2])
print(mytuple[0:3])
print(mytuple[:3])
print(mytuple[1:])

mytuple2=('tuple','list','string','boolean','integer','float')
print(type(mytuple2))
print(len(mytuple2))
print(mytuple2[4])
print(mytuple2[2:5])
print(mytuple2[:3])
print(mytuple2[4:])
mytuple3 = mytuple+mytuple2
print(mytuple3)


x = ('abi','sanjana','maran','anu','udhaiya')
y = list(x)
y[1] = "gayu"
x = tuple(y)
print(x)

updatetuple = ("maran",'kavin','praveen','shivesh')
y = list(updatetuple)
y.append("aashii")
updatetuple = tuple(y)
print(updatetuple)

z = ("manish",)
updatetuple += z
print(updatetuple)


x = list(updatetuple)
x.remove("manish")
updatetuple = tuple(y)

counttuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x =counttuple.count(8)
print(x)
r=counttuple.index(3)

del counttuple
print(counttuple)
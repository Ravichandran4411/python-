#set
thesett={"ravi","mani","guru","saravana","praba","sai","josh",'yash'}
thesett2={'praveen','shivesh','kavin',"manimaransanjana",'abimaran',"gayumani"}
thesett.update(thesett2)
print(thesett)
thesett.add("aashi") #add()
print(thesett)
thesett2.remove("abimaran") #remove()
print(thesett2)
thesett2.discard("manimaransanjana") #discard 
print(thesett2)
thesett2.pop() #pop()
print(thesett2)
clearset={"ktm",True,'mt50',34,6.9}
clearset.clear() #clear()
print(clearset)
thesett2.add(45)
print(thesett2)
thesett.remove("saravana")
print(thesett)
thesett.discard("sai")
print(thesett)
thesett.pop()
print(thesett)
loopset={1,2,34,5,6,7,8,9,10}
for i in loopset:
    print(i)
loopset.clear()
print(loopset)  
x = {"r", "m", "g"}
y = {"e", "p", "a",'g','r'}
z = x.union(y)   #union()
print(z)
a = {1,2,3,4,True,"s"}
b = {"t",5.67,34.56,45}
c = {23,56,"name",1,3,5,2,4}
d = a|b|c
print(d)
r=x.intersection(y)
print(r)
o=a & b & c
print(o)
del clearset
print(clearset)

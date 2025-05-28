thedict={"Name":"ravi",'age':17,'phoneno':9677073089}
a=thedict['Name']
print(a)
b=thedict.get('age')
print(b)
c=thedict.keys()
print(c)
d=thedict.values()
print(d)
thedict['maran']='udhaiya'
print(thedict)
e=thedict.items()
print(e)
thedict.update({'mani':'gayu'})
print(thedict)
thedict.pop("phoneno")
print(thedict)
thedict.popitem()
print(thedict)
for z,y in thedict.items():
    print(z,y)
thedict.clear()
print(thedict)
del thedict
print(thedict)    
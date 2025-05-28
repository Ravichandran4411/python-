# multiple data types in list
multi = ['sanjumanimaran', True, 304, 34.7, False, 'udhaiyamani']
string = []
inte = []
floa = []
boolean = []
for i in multi:
    if type(i) == str:
        string.append(i)
    elif type(i) == int:
        inte.append(i)
    elif type(i) == float:
        floa.append(i)
    else:
        boolean.append(i)
print(string)
print(inte)
print(floa)
print(boolean)
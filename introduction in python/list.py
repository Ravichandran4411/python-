###list
##
##
###index in list
##ml=['gayu','maran','anu']
##print(ml[2])
###range in list
##print(ml[1:3])
###without starting index
##print(ml[:1])
###without ending index
##print(ml[0:])
###change values in list
##ml[2]='sanjana'
##print(ml)
###append in list
##ml.append('gethapriya')
##print(ml)
###insert in list
##ml.insert(3,'dviyasri')
##print(ml)
###expand in list
##mll=["Manimaran","udhaiyasri","ragavi","tharnya","Mani"]
##ml.extend(mll)
##print(ml)
###remove in list
##ml.remove("maran")
##print(ml)
###pop in list
##ml.pop(8)
##print(ml)
###clear in list
##ml.clear()
##print(ml)
###del in list
##del ml
##print(ml)




#Calculate amounts in the list.
t=[1000,2000,3000,4000,5000]
s=0
for i in t:
    s+=i
print(s)

#Find Max element in the List.
element=[10,20,30,40,50]
maximumno=element[0]
for ma in element:
    if ma>maximumno:
        maximumno=ma
print(maximumno)

#Find Min element in the List.
element=[10,20,30,40,50]
minimumno=element[0]
for mi in element:
    if mi<minimumno:
        minimumno=mi
print(minimumno)        


#Find the odd number in another list
no=[1,2,3,4,5,6,7,8,9,10]
b=[]
for i in no:
    if i%2==1:
        b.append(i)
    elif i%2==0:
        b.append(i)
print(b)


#Find the even number in another list
numbers=[1,2,3,4,5,6,7,8,9,10]
b=[]
for even in numbers:
   if even%2==0:
       b.append(even)
print(b)

#multiple data types in list
multi=['sanjumanimaran',True,304,34.7,False,'udhaiyamani']
string=[]
inte=[]
floa=[]
boolean=[]
for i in multi:
    if type(i)==str:
        string.append(i)
    elif type(i)==int:
        inte.append(i)
    elif type(i)==float:
        floa.append(i)
    else:
        boolean.append(i)
print(string)
print(inte)
print(floa)
print(boolean)

        



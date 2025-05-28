# #even number from list
def eveno(x):
    return x%2 == 0
num = [2, 4, 5, 6, 7, 89, 5, 6, 7, 8, 9]
a=filter(eveno,num) 
print(list(a))


#words longer than 3 characters
def ch(z):
    return len(z)>3
words=['ravi','jai','bass','sai','guru','kavin','maran']
b=filter(ch,words)
print(list(b))

#remove empty string from a list using filter()
def str(n):
    return n!= ''
strin=['','maran','kavin','','','guru','ravi','']
c=filter(str,strin)
print(list(c))

#positive numbers from list using filter()
def pos(num):
    return num>0
integer=[-23,56,-7,-74,74,-23,-31,67]
d=filter(pos,integer)
print(list(d))


#name starts with "A"
def name(m):
    return m.startswith('A')
st=['Aashi',"Abimaran","Arun",'ravi','kavin','guru','Anumaran']
e=filter(name,st)
print(list(e))
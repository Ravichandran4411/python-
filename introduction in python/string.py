#string using index
#1
a='Ravichandran'
b=print(a[7])
#2
a='Manimaran'
b=print(a[8])
#3
a='Gurudev'
b=print(a[5])


#length of string
#1
a='Ravichandran'
b=print(len(a))
#2
a='Manimaran'
b=print(len(a))
#3
a='Gurudev'
b=print(len(a))


#loop using string
#1
a='Ravi'
for i in a:
    print(a)
#2
for i in "guru":
    print(i)
#3
for i in "mani":
    print(i)


#check in and not in
#1
a='Iam Ravichandran'
print('I' in a)
#2
a='Mani is a boy?'
if 'is' in a:
       print('yes! mani is a boy')
#3
a='Iam gurudev'
print('I' not in a)


#string slicing
#1
a='Ravichandran'
b=print(a[2:6])
#2
a='Gurudev'
b=print(a[3:6])
#3
a='Manimaran'
b=print(a[4:6])


#without starting index
#1
a='Ravichandran'
b=print(a[:8])
#2
a='Gurudev'
b=print(a[:6])
#3
a='Manimaran'
b=print(a[:5])


#without ending index
#1
a='Ravichandran'
b=print(a[2:])
#2
a='Gurudev'
b=print(a[3:])
#3
a='Manimaran'
b=print(a[4:])


#string in uppercase
#1
a='ravichandran'
b=print(a.upper())
#2
a='gurudev'
b=print(a.upper())
#3
a='manimaran'
b=print(a.upper())


#string in lower()
#1
a='RAVICHANDRAN'
b=print(a.lower())
#2
a='GURUdev'
b=print(a.lower())
#3
a='MaNiMaRaN'
b=print(a.lower())


#string strip()
#1
a=' good!  '
b=print(a.strip())
#2
a='bad!  '
b=print(a.strip())
#3
a=' ugly!'
b=print(a.strip())


#replace in string
#1
a='good '
b=print(a.replace('o','d'))
#2
a='bad'
b=print(a.replace('a','e'))
#3
a='ugly!'
b=print(a.replace('g','y'))


#split in string
#1
a='very,good'
b=print(a.split(','))
#2
a="good or bad or ugly"
b=print(a.split('or'))
#3
a='r and g and m'
b=print(a.split('and'))
        
        


#string concatenation
#1
a='r'
b='m'
c=a+b
print(c)
#2
a='good'
b='bad ugly'
c=a+" "+b
print(c)
#3
a='g'
b='d'
c=a+b
print(c)


#format in string
#1
a=24
b=f'my chemistry mark is {a}'
print(b)
#2
a=f'my name is ravi iam {2*9}'
print(a)
#3
a='ravi'
b=18
c=f'my name is {a} iam {b}'
print(c)


#escape string
#1
a='the \'cat\' is playing'
print(a)
#2
a='good\tbad\tugly'
print(a)
#3
a='my name is \'ravi\''
print(a)

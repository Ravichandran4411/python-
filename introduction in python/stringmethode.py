
s='1234Rvichandran!!'
print(s.isupper())
print(s.islower())
print(s.isalpha())
print(s.isalnum())
print(s.istitle())
print(s.isascii())
print(s.endswith('!'))
print(s.startswith('1'))
print(s.center(30,'$'))

a=' ravichandran  ' 
print(a.capitalize())
print(a.lstrip())
print(a.rstrip())
print(a.find('a'))
print(a.count('n'))
print(a.isalpha())
print(a.islower())

b='45657'
print(b.isdigit())
print(b.isnumeric())
print(b.isalnum())
print(b.endswith('!'))
print(b.startswith('5'))
print(b.find('4'))
print(b.count('5'))
print(b.lstrip())
print(b.rstrip())

c='IAM RAVICHANDRAN GOING TO SCHOOL'
print(c.isupper())
print(c.isdigit())
print(c.isnumeric())
print(c.istitle())

m=('r','m','g')
print('*'.join(m))

m=('dog','cat')
print('and'.join(m))

n='r\ta\tv\ti'
print(n.expandtabs(3))


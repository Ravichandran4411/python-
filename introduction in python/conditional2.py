###write a programm to calculate the grade using the given %
##a=int(input("enter your mark:"))
##if a>90:
##    print('a')
##elif a>80:
##    print('b')
##elif a>70:
##    print('c')
##elif a>60:
##    print('d')
##elif a>50:
##    print('e')
##else:
##    print('f')
##
##
###determines the tyoe of triangle based on side length
##a=int(input('enter length1:'))
##b=int(input('enter length2:'))
##c=int(input('enter length3:'))
##if a==b and b==c:
##    print('it is  isosceles')
##elif a==b or b==c or c==a:
##    print('it is equilateral')
##else:
##    print('it is rightangle triangle')
##
##
###check three persons salary and disply the minimum salary
##a=int(input('enter ravi salary:'))
##b=int(input('enter guru salary:'))
##c=int(input('enter mani salary:'))
##if a<b and a<c:
##    print("minimum salary:",a)
##elif b<a and b<c:
##    print("minimum salary:",b)
##else:
##    print("minimum salary:",c)
##
##
###determine the season using the given month
##a=input('enter any month:')
##if a in ('jan','feb','dec'):
##    print('winter season')
 
##elif a in('mar','apr','may','jun'):
##    print('summar season')
##elif a in ('jul','aug','sep'):
##    print('monsoon season')
##elif a in ('oct','nov'):    
##    print('rainy season')
##else:
##    print("invalid month")


#5
a=input('Enter any letter:')
if a in "aeiouAEIOU":
    print('IT IS VOWELS!')
else:
    print('IT IS CONSONANT')
 

#6
a=int(input('enter any year:'))
if a%4==0:
    print("IT IS A LEAP YEAR")
else:
    print('IT IS NOT A LEAP YEAR')

#7
a=int(input('enter any number:'))
if a%5==0 and a%3==0:
    print('it is divisible by 5 and 3')
elif a%5==0:
    print('it is only divisible by 5')
elif a%3==0:
    print('it is only divisible by 3')
else:
    print('given no is not divisible by 3 and 5')
    
#8    
a=int(input('enter a number:'))    
b=int(input('enter b number:'))
c=input('enter any operator:')
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='**':
    print(a**b)
elif c=='%':
    print(a%b)    
elif c=='/':
    print(a/b)
elif c=='//':
    print(a//b)    
else:
    print("invalid operator")


#9
a=int(input("enter a age:"))
if a>=18:
    print('eligible to vote')
else:
    print('not eligible to vote')
    
    
#10
a=int(input("enter the day:"))
if a==1:
    print("sunday")
elif a==2:
    print("monday")
elif a==3:
    print('tuesday')
elif a==4:
    print('wednesday')
elif a==5:    
    print("thursday")
elif a==6:
    print('friday')
elif a==7:
    print('saturday')
else:    
    print('invalid output')

#11
a=int(input('enter a value1'))    
b=int(input('enter a value2'))    
c=int(input('enter a value3'))    
d=a+b+c
if d<=180:
    print('it is valid triangle!')
else:
    print('it is invalid triangle!')

#12
a=int(input('enter any number:'))
if a<10:
    print('ones')
elif a<100:
    print('twos')
else:
    print('invalid output')




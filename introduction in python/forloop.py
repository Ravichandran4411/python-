###print all the numbers from 1-15
##
##for i in range(1,16): 
##    print(i)
##
##
###print odd numbers from 6-29
##
##for i in range(6,30):
##    if i%2!=0:
##        print(i)
##
##
###print even numbers from 20-40
##
##for i in range(20,40):
##    if i%2==0:
##        print(i)
##
##
###it is divisible by 3 and 5
##
##for i in range(1,16):
##    if i%5==0 and i%3==0:
##        print('the no is divisible by 5 and 3:',i)
##    elif i%5==0:
##        print('the no is divisible by 5:',i)
##    elif i%3==0:
##        print('the no is divisible by 3:',i)
##       
##
##
###print all the elements of an list
##
##a=['r','m','g']
##for i in a:
##    print(i)
##
##
###calculate sum of all elements in an list
##
##a=[10,20,30,40]
##s=0
##for i in a:
##    s+=i
##print(s)
##
##
###calculate the sum of all numbers from 1 to 100
##s=0
##for i in range(1,101):
##   s=s+i
##print(s)   
##
##
###calculate the factorial of a given number
##
##a=int(input('enter any number:'))
##f=1
##for i in range(1,a+1):
##    f*=i
##print(f)
##
##
###find maximum element in an list
##a=[1000,20000,300000,4000000,5000000]
##m=a[0]
##for i in a:
##    if m<i:
##        m=i
##print(i)        


###print a pattern of * in a triangle shape
##r=5
##for i in range(1,r+1):
##    print('*'*i)


#1
r=5
for i in range(1,r+1):
    print(" "*(r-i)+'*'*i)

#2
r=5
for i in range(1,r):
    print('*'*r)
 
#3
for i in range(4):
    if i==0 or i==3:
        print('****')
    else:
        print('*  *')
     

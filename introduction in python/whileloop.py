###mulitiplication of a table
##
##a=int(input('enter any number:'))
##i = 1
##while i <= 10:
##    print(f"{a} x {i} = {a * i}")
##    i += 1
##
###print numbers from 1 to 10
##
##i=1
##while i<11:
##    print(i)
##    i+=1
##
###sum of frist from n natural numbers
##
##a=int(input('enter any number:'))
##i=1
##b=0
##while i<=a:
##    b+=i
##    i+=1
##print(a,b)    
##
###factorial of a number
##
##a=int(input("Enter a number: "))
##f=1
##i=1
##while i<=a:
##    f*= i
##    i += 1
##print(f"The factorial of {a} is {f}")
##
###print even numbers from 1 to 100
##
##i=0
##while i<100:
##    i+=1
##    if i%2==0:
##        print(i)
##        
###6 odd numbers from 1 to 100
##        
##i=0
##while i<100:
##    i+=1
##    if i%3==0:
##        print(i)
##
###7check the number is pannlindrome
##        
##a = int(input("Enter a number: "))
##o_n = a
##r_n = 0
##while a > 0:
##    digit=a%10
##    r_n=r_n*10+digit
##    a=a//10
##if o_n == r_n:
##    print(f"{o_n} is a palindrome.")
##else:
##    print(f"{o_n} is not a palindrome.")
##
###8check if a number is Amstrong number
##    
##num = int(input("Enter a number: "))
##on = num
##n_digits = len(str(num))
##sum_of_powers = 0
##while num > 0:
##    digit = num % 10
##    sum_of_powers += digit ** n_digits
##    num //= 10
##if sum_of_powers == on:
##    print(f"{on} is an Armstrong number.")
##else:
##    print(f"{on} is not an Armstrong number.")
    
###9 reverse a number
##    
##num = int(input("Enter a number: "))
##on = num
##rn = 0
##while num > 0:
##    digit = num % 10
##    rn = rn * 10 + digit
##    num = num // 10
##print(rn)

###10 all prime number 1 to 100
##
##a = 2  
##while a <= 100:
##    is_prime = True
##    i = 2
##    while i * i <= a:
##        if a % i == 0:
##            is_prime = False
##            break
##        i += 1
##    if is_prime:
##        print(a, end=" ")
##    a += 1    
##


#
for i in range(1,50):
    if i%15==0:
        print('fizzbuzz',i)
    elif i%3==0:
        print('fizz',i)
    elif i%5==0:
        print('buzz',i)
    
    


    

#Match case in python

###1
op = input("Enter an operator: ")
a = 2
b = 100
match op:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case _:
        print('invalid output')

###2
a=int(input("enter any number:"))
match a>=0:
    case True:
        print("it is +ve number!")
    case False:
        print("it is -ve number!")
    case _:
        print('invalid output')    


###3
a=int(input("enter a no:"))
b=int(input("enter b no:"))
match a>b:
    case True:
        print("a is greater than b")
    case False:
        print("b is greater than a")
    


###4
a=input("enter any month:")
match a:
    case "jan"|"feb"|"dec":
         print('winter season')
    case "mar"|"apr"|"may"|"jun":
         print('summar season')
    case "jul"|"aug"|"sep":
         print('monsoon season')
    case "oct"|"nov":
         print('rainy season')
    case _:
         print('invalid month')


###5
a=int(input('enter a date'))
match a:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
    print('invalid output')


###6
l=int(input('enter a year:'))
match l%4==0:
    case True:
        print("it is leap year!")
    case False:
       print("it is not a leap year!")

       
###7
v=int(input('enter your age:'))
match v>=18:
    case True:
        print("YOUR ELIGIBLE TO VOTE")
    case False:
        print("YOUR NOT ELIGIBLE TO VOTE")
    case _:
        print('INVALID AGE')

        
###8
a=input('enter any letter:')
match a in "aeiouAEIOU":
    case True:
        print("IT IS A VOWELS")
    case False:
        print("IT IS A CONSONANT")


###9
a=int(input("enter any number:"))
match a%5==0 and a%3==0:
    case True:
        print("the no is divisible by 5 amd 3")
    case False:
        print("the no is not divisible by 5 and 3")
match a%5==0:
    case True:
        print("the no is divisible by 5 ")
match a%3==0: 
    case True:
        print("the no is divisible by 3 ")


##10
a=int(input('enter any number:'))
match a<=10:
    case True:
        print("ones")
    case False:
        print("twos")
        
        

    
        

        
    

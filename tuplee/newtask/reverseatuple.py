tuplee = (1,2,3,4,5,6,7,8,9,10) 
reverse_tuplee= []
for i in range(len(tuplee)-1, -1, -1):
    reverse_tuplee.append(tuplee[i])
a=tuple(reverse_tuplee)    
print("Reverse a list:", a)

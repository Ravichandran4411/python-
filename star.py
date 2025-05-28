#1
a = int(input("Enter the number of rows"));
for i in range(0, a):
	for j in range(0, a-i-1):
		print(end=" ")
	for j in range(0, i+1):
		print("*", end=" ")
	print()

#2

a=int(input(" enter the number of rows"));
for i in range(a,0,-1):
    for j in range(0, a-i):
        print(end=" ")
    for j in range(0,i):
        print("* ", end=" ")
    print()

#3

a = int(input("enter the no of rows"));
for i in range(a,0,-1):
    for j in range(0, a-i):
        print(end=" ")
    for j in range(0,i):
        print("* ", end=" ")
    print()    

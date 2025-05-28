number = int(input("enter any number:"))
mytpl = (1, 2, 3, 4, 5, 6, 7, 7, 48, 56, 43, 56, 6, 7, 74, 36, 39, 456)
if number in mytpl:
    print(f'the {number} in a tuple')
else:
    print(f'the {number} is not in tuple')

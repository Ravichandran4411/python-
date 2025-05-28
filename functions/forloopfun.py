# 1  print one to ten using loop in funtions

def onetoten():
    for i in range(1, 11):
        print(i)
onetoten()

# 2  print odd number from 6 to 29


def sixtothirty():
    for i in range(6, 30):
        if i % 2 == 1:
            print(i)


sixtothirty()

# 3  print even number from 20-40


def evennumbers():
    for i in range(20, 41):
        if i % 2 == 0:
            print(i)


evennumbers()

# 4  div by only 3


def divby3():
    for i in range(1, 15):
        if i % 3 == 0:
            print(i)


divby3()

# 6  div by 6


def divby6():
    for i in range(1, 15):
        if i % 6 == 0:
            print(i)


divby6()

# 7  divby 3 and 6


def divby3and6():
    for i in range(1, 16):
        if i % 3 == 0 and i % 6 == 0:
            print(i)


divby3and6()


# 8  sum of elements in the list


def sumodlist(lst):
    listt = [2, 3, 4, 5, 8, 9]
    sum = 0
    for i in lst:
        sum += i
    print(sum)
sumodlist(sum)
  
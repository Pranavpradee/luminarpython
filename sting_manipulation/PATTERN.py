#a=int(input("enter a no :"))
"""for i in range(5,0,-1):
    for j in range (0,i):
        print("*",end=" ")
    print()"""


#NUMBER

"""for i in range(0,5):
    for j in range(i):
        print(i,end=" ")
    print()"""

#NUMBER_IN_REVERSE

"""for i in range(5,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()"""

#USING FUNCTION

"""def pattern(row):
    for i in range(row,5):
        for j in range (0,i):
            print("*",end=" ")
        print()
pattern(0)"""

#

"""def pattern(n):
    num=1
    for i in range (5):
        num=1
        for j in range (i):
            print(num,end=" ")
            num+=1
        print("\r")
pattern(6)
"""
#

def pattern (n):
    num=1
    for i in range(5):
        for j in range(i):
            print(num,end=" ")
            num+=1
        print()
pattern(5)

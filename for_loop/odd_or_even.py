"""n1=int(input("enter a number :"))
if n1>0:
    if n1 % 2 ==0:
        print("num is even")
    else:
        print("num is odd")
else:
    print("please enter a positive no")"""
n1=int(input("enter the min range :"))
n2=int(input("enter the max range "))
for i in range (n1,n2+1):
    if i%2==0:
        print (i)

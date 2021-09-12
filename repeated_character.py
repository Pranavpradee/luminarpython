"""a="apple"
b=""
for i in a:
    if i not in b:
        b=b+i
    else:
        print("firsr recursive character ",a,"is=",i)"""

#OR


a=input("enter the string:")
b=""
for i in a:
    if i not in b:
        b=b+i
    else:
        print("fist recursive character",a,"is=",i)
        break
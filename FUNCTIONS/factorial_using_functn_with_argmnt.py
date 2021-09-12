"""def factorial(fact):
    s=1
    if fact>0:
        for i in range (1,fact+1):
            s=s*i
            print(s)

    elif fact==0:
        print("factrial of 0 is 1")
    else:
        print("factorial doesnot exist for negative numbers")

factorial(5)"""


#using_return
def factorial(fact):
    s=1
    if fact>0:
        for i in range (1,fact+1):
            s=s*i
            return s
    elif fact ==0:
        return "factorial of0 is 1"
    else:
        return "factorial doesnt exist"
print(factorial(5))






n=int(input("enter a no"))
if n>0:
    fact=1
    for i in range(1,n+1):
        fact=fact*1
        print(fact)
elif n ==0:
    print("fact of 0 is 1")
else:
    print("fact doesnt exist for -ve no.")


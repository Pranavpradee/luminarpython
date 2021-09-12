s={1,2,3,4,5,6,66,77,88,33,22,11,34}
prime=set()
notprime=set()
for i in s:
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                notprime.add(i)
                break
        else:
            prime.add(i)
print(prime)
print(notprime)


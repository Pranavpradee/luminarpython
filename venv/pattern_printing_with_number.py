# pattern printing exm


#
# def pattern():
#     n = int(input("enter the initial range"))
#     p = int(input("enter the final value"))
#
#     for i in range(0,p):
#         for j in range(0, i + 1):
#             print(n, end=" ")
#         print("\r")
#
#     n=n+1
#     for i in range(p, 0, -1):
#         for j in range(n, i+1):
#             print(n, end=" ")
#         print("\r")
#     n = n + 1
#     for i in range(0,p):
#         for j in range(0, i + 1):
#             print(n, end=" ")
#         print("\r")
#     n = n + 1
#     for i in range(p, 0, -1):
#         for j in range(n, i + 1):
#             print(n, end=" ")
#         print("\r")
#
#
#
#
#
# pattern()



# k=int(input("enter the initial value"))
# p=int(input("enter the final value"))
# for i in range (k,p):
#     for r in range (p):
#         print(end=" ")
#     p=p+1
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

#


# eliminate duplicate elements

# lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# print(list(set(lst)))



# a=[]
# [a.append(i) for i in lst if i not in a ]
#                          # for i in lst:
#                               #      if i not in a:
#                                        #         a.append(i)
# print(a)


# REMOVING VOWEL FROM A STRING

# A = input("Enter the String: ")
#
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# b = ""
# length = len(A)
#
# for i in range(length):
#     if A[i] not in vowels:
#         b = b + A[i]
#
# print("\nString after removing Vowels: ")
# A = b
# print(A)

#comprehension

#
# a=[i for i in range(1,100) if i%5==0]
# print (a)

#sumofprime
#
# def prime(n):
#   prime=[True]*(n+1)
#   p=2
#   while p*p<=n:
#       if prime[p]==True:
#           i=p*2
#           while i<=n:
#               prime[i]=False
#               i+=p
#       p+=1
#   sum=0
#   for i in range (2,n+1):
#       if prime[i]:
#           sum+=i
#   return sum
# print(prime(50))

#or
#
# def sumprime(min,max):
#     sum=0
#     for a in range(min,max):
#         if a>1:
#             for i in range (2,a):
#                 if (a%i)==0:
#                     break
#             else:
#                 sum=sum+a
#     return sum
# print (sumprime(1,50))



a=int(input("enter the initial value"))
b=int(input("enter the final value"))
r=5
for i in range(a,b):
    if (i%2==0):
        #print (i)
        for k in range (r,0,-1):
            for j in range(0,k):
                print(i,end=" ")
            print("\r")
    else:
        for l in range(r):
            for m in range(0,l+1):
                print(i,end=" ")
            print("\r")

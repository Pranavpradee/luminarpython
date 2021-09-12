# def prime(n1,n2):
#     flag=0
#     if n1>1:
#         for i in range (2,n1):
#             if n1%i==0:
#                 break
#             else:
# #
#     if i in "aeiou":
#
# else:
#
#    print(a)

# Program make a simple calculator

# This function adds two numbers
# def add(x, y):
#     return x + y
#
#
#
# def subtract(x, y):
#     return x - y
#
#
#
# def multiply(x, y):
#     return x * y

# b=[i for i in range (1,100) if i/5==0]
# print(b)
# #
# t({lst[]}
# lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# prin
# a=int(input("enter string"))
# for i in a:
#     if i in "aeiou":
#         i.remove("aeiou")
#         print (i)


lst = [1, 0, 7, 5, 9, 2, 3, 5, 7, 2, 0, 1, 10]

temp = []

for i in lst:
    if i not in temp:
        temp.append(i)

lst = temp

print("List After removing duplicates ", lst)
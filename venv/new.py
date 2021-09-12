

# pattern printing exm

def pattern():
    n=int(input("intial value"))
    p=int(input("final value"))
    for i in range(0, p):
        for j in range(0, i + 1):
            print(n, end=" ")
        print("\r")
    n=n+1
    for i in range(p, 0, -1):
        for j in range(n, i+1):
            print(n, end=" ")
        print("\r")


pattern()


# reverse
#
# p=int(input("enter the inittial value"))
# n=int(input("enter the final value"))
# def pattern():
#     x = 0
#     for i in range(p , n+1):
#         x += 1
#         for j in range(p, i + 1):
#             print(p, end=" ")
#         for i in range(n, 0, -1):
#             for j in range(1, i + 1):
#                 print(j, end=" ")
#         print("\r")
# pattern()

# def pattern(n):
#     for i in range(n, 0, -1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#
#         print("\r")
#
#
# pattern(5)



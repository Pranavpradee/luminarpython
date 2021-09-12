# k=5
# for i in range (5):
#     for r in range(k):
#         print(end=" ")
#     k-=1
#     for j in range (0,i+1):
#         print("*",end=" ")
#     print()

def parallel(n):
    k=n
    for i in range (n):
        for r in range (k):
            print(end=" ")

        k+=1
        for j in range (0,n):
                print("*",end=" ")
        print()
parallel(6)
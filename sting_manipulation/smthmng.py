def pattern(n):
    num=0
    for i in range (n):
        num=0
        for j in range (i):
            num+=1
            print(num,end=" ")
        print()
pattern(5)

list1=[1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]
def linearsearch(list1):
    elemnt=int(input("enter the elemnt :"))
    flag=0
    for i in list1:
        if i==elemnt:
            flag=1
            break
    if flag==0:
        print("not found")
    else:
        print("found")


linearsearch(list1)
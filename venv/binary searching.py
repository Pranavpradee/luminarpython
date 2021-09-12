lis=[1,6,5,8,7,9,10,11,12,13,14,15,16,17,18,19]
def bsearch():
    lis.sort(lis)
    print(lis)
    ele=int(input("enter the elemnt"))
    flag=0
    low=0
    uppr=len(list)-1
    while low<=uppr:
        mid=(low+uppr)//2
        if ele>list[mid]:
            low=mid+1
        elif ele<list[mid]:
            uppr=mid-1
        elif ele==lis[mid]:
            flag=1
            break
    if flag==1:
        print("found")
    else:
        print("not found")
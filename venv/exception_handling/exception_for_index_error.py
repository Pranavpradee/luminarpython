# lst=[1,2,3]
# index=int(input("enter the index"))
# try:
#     print(lst[index])
# except:
#     print("index not exist in list")
#
# finally:
# #     print("condition is inside the list5")



# lst=[1,2,4,5]
# pos=int(input("enter the index"))
# try:
#     print(lst[pos])
# except Exception as e:
#     print(e.args)
# finally:
#     print("inside")



n1=int(input("enter n1"))
n2=int(input("enter n2"))
try:
    res=n1/n2
    print(res)
except Exception as e:
    print(e.args)
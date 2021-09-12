d={1:10,2:20,3:30,4:40,5:50}
def a(x):
    if x in d:
        print(x,'is present')
    else:
        print(x,'not present')
x=int(input("enter the key"))
a(x)

import re
n="hello"
x='\w+'# we can use[a=z]+ alse
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")

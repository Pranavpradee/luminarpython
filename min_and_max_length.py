import re
n=input("enter a num:")
x='[\D]{8,15}'                              #OR       # x='[a-zA-Z][^0-9\w]{8,15}'
match= re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")

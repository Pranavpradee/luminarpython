# import re
# n=input("enter reg no:")
# x='[A-Z]{2}\d{2}[A-Z]{2}\d{4}$'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

import re
n=input("enter reg no:")
x='[a-zA-Z]+\d{1}$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
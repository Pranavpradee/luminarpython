import re
f1=open("phn_num",'r')
x="[+][9][1][0-9]{10}$"
for num in f1:
    number=num.rstrip("\n")
    matcher=re.fullmatch(x,number)
    if matcher !=None:
        print(num)



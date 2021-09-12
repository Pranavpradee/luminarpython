"""a="apple"
vowels=0
for i in a:
    if(i=='a'or i=='e'or i=='i'or i=='o'or i=='u'or i=='A' or i=='E'or i=='I'or i=='O'
    or i=='U'):
        vowels=vowels+1
print(vowels)"""

#OR


a=input("enter the string")
count =0
for i in "aeiou":
    count+=1
else:
    pass
print("no. of vowels in",a,'is=',count)

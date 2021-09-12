class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name)
        print(self.age)
st1=open('file_prblm','r')
for line in st1:

#     print(line)
    l=line.split(",")
    name=l[0]
    age=l[1]

    st=Student(name,age)
    print(st)
    st.printval()



class Student:
    def __init__(self,name,deprtmnt,rollno,mark):
        self.name=name
        self.rollno=rollno
        self.deprtmnt=deprtmnt
        self.mark=mark
    def printval(self):
        print("name",self.name)
        print("rollno",self.rollno)
        print("department",self.deprtmnt)
        print("mark",self.mark)
    def __str__(self):
        return self.name
    f=open("file_prblm","r")
    for line in f:
        data=line.split(",")
        name=data[0]
        rollno=data[1]
        course=data[2]
        mark=data[3]
        obj=Student(name,rollno,course,mark)
        print(obj)
        obj.printval()

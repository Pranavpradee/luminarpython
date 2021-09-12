# class Student:
#     college="JECC"
#     def __init__(self,name,rollno,departmnt):
#         self.name=name
#         self.rollno=rollno
#         self.departmnt=departmnt
#
#     def printval(self):
#         print(self.name,self.rollno,self.departmnt)
#         print(Student.college)
#     def __str__(self):
#         return self.name+str(self.rollno)
# st=Student("pranav",65,"ece")
# st.printval()
# print(st)
class Parent:
    def __init__(self,name,adrs):
        self.name=name
        self.adrs=adrs
    def printval(self):
        print(self.name,self.age)
class Teacher(Parent):
    def __init__(self,id,deprtmnt,name,adrs):
        self.id=id
        self.deprtmnt=deprtmnt
    def print(self):
        print(  self.name,self.id,self.departmnt,self.subject)


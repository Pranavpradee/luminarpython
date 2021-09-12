# class Student:
#     def setvalue(self,name,rollno,schoolname):
#         self.name=name
#         self.rollno=rollno
#         self.schoolname=schoolname
#     def printvalue(self):
#         print("name",self.name)
#         print("rollno",self.rollno)
#         print("school name",self.schoolname)
# stud=Student()
# stud.setvalue("pranav",68,"ghsscpy")
# stud.printvalue()
# std=Student()
# std.setvalue("pooja",68,"JECC")
# std.printvalue()



class Student:
    schoolname='jecc'
    def setvalue(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def printvalue(self):
        print("name",self.name)
        print("rollno",self.rollno)
        print("school name",Student.schoolname)
stud=Student()
stud.setvalue("pranav",68)
stud.printvalue()
std=Student()
std.setvalue("pooja",68)
std.printvalue()

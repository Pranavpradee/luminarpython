class Person:
    def __init__(self,name,age):
        self.name=name
    #
    #     def printval(self):
    #         print("name", self.name)
    #         print("age", self.age)
    #
    # class Student(Person):
    #     def __init__(self, rollno, mark, name, age):
    #         super().__init__(name, age)
    #         self.rollno = rollno
    #         self.mark = mark
    #
    #     def print(self):
    #         print(self.name)
    #         print(self.age)
    #         print(self.rollno)
    #         print(self.mark)
    #
    # cr = Student(22, 75, "pranav", 22)
    # cr.printval()
#     self.age=age
#
# cr.print()


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name",self.name)
        print("age",self.age)
class Employee(Person):
    def __init__(self,id,salary,deptmnt,name,age):
        super().__init__(name,age)
        self.id=id
        self.salary=salary
        self.deptmnt=deptmnt
    def print(self):
        print(self.id)
        print(self.salary)
        print(self.deptmnt)
emp=Employee(1160,25000,"ece","pranav",22)
emp.printval()
emp.print()
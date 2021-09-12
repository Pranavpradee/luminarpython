# class Person:
#     def setval(self,name,age,adrs):
#         self.name=name
#         self.age=age
#         self.adrs=adrs
#         print(self.name,self.age,self.adrs)
# class Employee(Person):
#     def set(self,id,salary,department):
#         self.id=id
#         self.salary=salary
#         self.depatment=department
#
#         print(self.age)
#         print(self.salary)
#         print(self.department)
#         print(Person.name)
# emp=Employee()
# emp.setval("pranav",22,"kizhur")
# emp.set(2213,45000,"it")

#
# class Person:
#     def set(self,name,age,adrs):
#         self.name=name
#         self.age=age
#         self.adrs=adrs
#         print(self.name,self.age,self.adrs)
class Child:
    def setval(self,school,std):
        self.school=school
        self.std=std
        print(self.school,self.std)
class Student(Person,Child):
    def printval(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.rollno,self.mark)
st=Student()
st.set("pranav",21,"abc")
st.setval("luminr",11)
st.printval(2,98)





class Person:
    def set(self,name,age,adrs):
        self.name=name
        self.age=age
        self.adrs=adrs
        print(self.name,self.age,self.adrs)
class Parent:
    def setval(self,name,age):
        self.name=name
        self.age=age

class Employee(Person,Parent):
    def set(self,id,salary,department):
        self.id=id
        self.salary=salary
        self.depatment=department
# class A:
#     def printA(self):
#         print("inside A")
# class B(A):
#     def printB(self):
#         print("inside B")
# class C(B):
#     def print(self):
#         print("inside C")
# a=A()
# a.printA()
# b=B()
# b.printB()
# b.printA()
# c=C()
# c.printC()
# c.printB()
# c.printA()

#
# class Person:
#     def set(self,name,age,addrs):
#         self.name=name
#         self.age=age
#         self.addrs=addrs
#         print(self.name,self.age,self.addrs)
# class Child(Person):
#     def setval(self,school,std):
#         self.school=school
#
#         self.std=std
#         print(self.school,self.std)
# class Student(Child):
#
#     def seta(self,rollno,mark):
#
#         self.rollno=rollno
#         self.mark=mark
#         print(self.rollno,self.mark)
# st=Student()
# st.set("pra",22,"kizhu")
# st.setval("jecc",10)
# st.seta(11465,75)




class Person(Student):
    def set(self,name,age,addrs):
        self.name=name
        self.age=age
        self.addrs=addrs
        print(self.name,self.age,self.addrs)
class Child(Student):
    def setval(self,school,std):
        self.school=school
        self.std=std
        print(self.school,self.std)
class Parent:
    def setx(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Student(Child):

    def seta(self,rollno,mark):

        self.rollno=rollno
        self.mark=mark
        print(self.rollno,self.mark)
c=Child()
b=Student()
c.set("pra",22,"kizhu")
c.setval("jecc",10)

c.seta(1245,85)
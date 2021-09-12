# class employee:
#     def setvalue(self,name,salary,age,department):
#         self.name=name
#         self.salary=salary
#         self.age=age
#         self.department=department
#     def printvalue(self):
#         print("name",self.name)
#         print("salry",self.salary)
#         print("age",self.age)
#         print("department",self.department)
# emp=employee()
# emp.setvalue("pranav",25000,22,"ECE")
# emp.printvalue()


class addition:
    def setvalue(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print(self.n1+self.n2)

a=addition()
n1=int(input("enter"))
n2=int(input("enter"))
a.setvalue(n1,n2)

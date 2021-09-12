class Employee:
    companyname="UST GLOBAL"
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def printval(self):
        print("name",self.name)
        print("age",self.age)
        print("salary",self.salary)
        print("cmpnyname",Employee.companyname)
emp=Employee("PRANAV",22,25000)
# emp.setval("PRANAV",22,25000)
emp.printval()
em=Employee("pooja",25,30000)
# em.setval("pooja",23,30000)
em.printval()

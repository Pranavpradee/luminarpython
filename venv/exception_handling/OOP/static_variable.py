class Employee:
    companyname="UST GLOBAL"
    def setval(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def printval(self):
        print("name",self.name)
        print("age",self.age)
        print("salary",self.salary)
        print("cmpnyname",Employee.companyname)
emp=Employee()
emp.setval("PRANAV",22,25000)
emp.printval()
em=Employee()
em.setval("pooja",23,30000)
em.printval()

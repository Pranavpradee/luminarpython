# class Person:
#     def printval(self,name):
#         self.name=name
#         print("inside person method",self.name)
# class Child(Person):
#     def printval(self,class1):
#         self.class1=class1
#         print("inside child method",self.class1)
# ch=Child()
# ch.printval("abcd")



class Operators:
    def printvalue(self,name,adrs):
        self.name=name
        self.adrs=adrs
        print("its the first",self.name,self.adrs)
class Person(Operators):
    def printvalue(self,class1,class2):
        self.class1=class1
        self.class2=class2
        print("its the second",self.class1,self.class2)
pe=Person()
pe.printvalue("pranav","kizhur")
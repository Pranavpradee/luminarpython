# class book:
#     def reading(self):
#         print("person is reading")
#     def throw(self):
#         print("person is throwing the book")
# bk1=book()
# bk1.reading()
# bk1.throw()
#
#
# bk2=book()
# bk2.reading()
# bk2.throw

class person:
    def setvalue(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
        print("name",self.name)
        print("age",self.age)
pe=person()
pe.setvalue("anu",26)
pe.printvalue()
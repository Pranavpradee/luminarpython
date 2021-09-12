class Bank:
    bankname="SBI"
    def accreate(self,acno,name):
        self.acno=acno
        self.name=name
        self.minbal=5000
        self.balance=self.minbal

    def deposit(self,amt):
        self.amt=amt
        self.balance+=self.amt
        print(bankname,"your account has credited with amount",self.amt)
        print("your current balance=",self.balance)
    def withdraw(self,amnt):
        self.amnt=amnt
        if self.amnt>self.balance:
            print("insufficient balance")
        else:
            print
#
#
#         print(Bank.balance+self.deposit)
#         print(Bank.balance-self.withdrawal)
# ban=
#


#
# class Person:
#     def __init__(self,name,age,address):
#         self.name=name
#         self.age=age
#         self.address=address
#     def printval(self):
#         print(self.name,self.age,self.address)
# obj=Person("pranav",22,"aniyath house,kizhur")
# obj.printval()


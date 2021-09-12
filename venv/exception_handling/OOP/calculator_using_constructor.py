class Calculator:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def printval(self):

        print("1) addition""\n""2) subtraction""\n""3) multiplication""\n""4) division")
        choice = int(input("choose an operation to perform"))

        if choice==1:
            print(self.n1+self.n2)
        elif choice==2:
            print(self.n1-self.n2)
        elif choice==3:
            print(self.n1*self.n2)
        elif choice==4:
            print(self.n1/self.n2)
        else:
            print("invalid")
n1=int(input("enter the no"))
n2=int(input("enter the no"))
cal=Calculator(n1,n2)
cal.printval()
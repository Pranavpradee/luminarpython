class Vehicle:
    def __init__(self,model,regno,colour):
        self.model=model
        self.regno=regno
        self.colour=colour
    def printval(self):
        print(self.model)
        print(self.regno)
        print(self.colour)
veh=Vehicle("royal enfield","KL51A45602","red")
veh.printval()
print(veh)
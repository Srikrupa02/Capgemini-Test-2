class Car:
    def __init__(self):
        print("Car")
    def showC(self):
        print("Car moves on land")
class Airoplane:    
    def __init__(self):
        print("Airoplane")
    def showA(self):
        print("Aioplane moves in air")
class Flying_car(Car,Airoplane):
    def __init__(self):
        super().__init__()
        print("Flying Car")
    def showF(self):
        print("Flying car can move both on land and air")  
f=Flying_car()
f.showF()
f.showA()
f.showC()
class Vehicle:
    def __init__(self):
        print("--vehicle---")
    def showV(self):
        print("Vehicles are of many types")
class Car(Vehicle):
    def __init__(self):
        super().__init__() 
        print("--car---")
    def showC(self):
        print("Car has capacity of 5 members")
class Bike(Vehicle):
    def __init__(self):
        super().__init__() 
        print("-----")
    def showB(self):
        print("Bike has only capaity of 2 members")
class Electric_car(Car):
    def __init__(self):
        super().__init__() 
        print("--electric car---")
    def showE(self):
        print("Electric car has only capaity of 10 members")
e=Electric_car()
e.showV()
e.showC()
e.showE()
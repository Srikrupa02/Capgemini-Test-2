 #Build a `SmartPhone` class inheriting from `MobileDevice`, 
 # which in turn inherits from `Electronics`. 
 # Demonstrate method overriding and attribute reuse.
class Electronics():
    def __init__(self,name):
        self.name=name
        print("Electronic devices consists of Mobiles and SmartPhones ")
    def showE(self):
        print(f"The device is:{self.name}")
class Mobile(Electronics):
    def __init__(self,name,cost):
        super().__init__(name)
        self.cost=cost
        print("Mobiles are of many models")
    def showM(self):
        print(f"Mobile cost is:{self.cost}")
class Smartphone(Mobile):
    def __init__(self,name,cost,model):
        super().__init__(name,cost)
        self.model=model
        print("Samsung is best of any other mobiles")
    def showS(self):
        print(f"Samsung model is:{self.model}")
s=Smartphone("Samsung",20000,"s23")
s.showS()
s.showM()
s.showE()


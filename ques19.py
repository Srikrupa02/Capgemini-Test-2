from abc import ABC,abstractmethod
class IVehicles:
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class Car(IVehicles):
    def start_engine(self):
        print('Car engine has started')
    def stop_engine(self):
        print('Car engine has stopped')
class Bike(IVehicles):
    def start_engine(self):
        print('Bike engine has started')
    def stop_engine(self):
        print('Bike engine has stopped')
class Truck(IVehicles):
    def start_engine(self):
        print('Truck engine has started')
    def stop_engine(self):
        print('Truck engine has stopped')
car=Car()
car.start_engine()
car.stop_engine()
bike=Bike()
bike.start_engine()
bike.stop_engine()
truck=Truck()
truck.start_engine()
truck.stop_engine()

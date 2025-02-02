#Implement an abstract class `ICalculator` with methods `add()`, `subtract()`, `multiply()`, and `divide()`. 
# Create a `BasicCalculator` class that implements these methods.
from abc import ABC, abstractmethod
class ICalculator(ABC):
    @abstractmethod
    def add(self,num1,num2):
        pass 
    @abstractmethod
    def sub(self,num1,num2):
        pass 
    @abstractmethod
    def mul(self,num1,num2):
        pass 
    @abstractmethod
    def div(self,num1,num2):
        pass 
class Basic_calculator(ICalculator):
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def showAdd(self):
        add=self.num1+self.num2
        print(f"The sum of no's is:{add}")
    def sub(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def showSub(self):
        sub=self.num1-self.num2
        print(f"The sub of no's is:{sub}")
    def mul(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def showMul(self):
        mul=self.num1*self.num2
        print(f"The mul of no's is:{mul}")
    def div(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def showDiv(self):
        div=self.num1/self.num2
        print(f"The div of no's is:{div}")
calci=Basic_calculator()
calci.add(4,5)
calci.showAdd()
calci.sub(5,4)
calci.showSub()
calci.mul(4,5)
calci.showMul()
calci.div(4,2)
calci.showDiv()
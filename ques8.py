class Animal:
    def __init__(self):
        print("Animal")
    def speak(self):
        print("Animals can make sounds")
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog")
    def speak(self):
        print("Dog says Bow Boww")
class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("Cat")
    def speak(self):
        print("Cat says Meow Meow")
c=Cat()
c.speak()
d=Dog()
d.speak()

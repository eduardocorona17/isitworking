class Dog:
    """simple class representing a dog"""
    def __init__(self, name, age):
        """Initialize name + age attributes"""
        self.name = name
        self.age = age
    def sit(self):
        """simulating a dog sitting"""
        print(f"{self.name} is now sitting.")

    def bark(self):
        """simulate dog barking."""
        print(f"{self.name} can you please not? Its 3 am!")

my_dog = Dog("Sammi", 3)
# print(my_dog.bark())
my_dog.bark()
my_dog.sit()
your_dog = Dog("Luna", 4)
your_dog.bark()

class Car:
    """Emulate a vehicle"""
    def __init__(self, make, model, color):
        """Initialize make, model, color"""
        self.make = make
        self.model = model
        self.color = color
        self.accelarate = ""
    
    def vroom(self):
        print(f"My {self.model} go vroom lol!")

F_150 = Car("Ford", "F-150", "Black")
F_150.vroom()


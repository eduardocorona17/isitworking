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
#  OOP Lesson 1

# Class blueprint for animal
# class Animal():
#     def __init__(self):

# Class blueprint for a Cat
class Cat():#Animal):
    # Constructor method to initialize object
    def __init__(self, kind="cat", name="", age=0, colour=""):
        # initialize attributes
        self.kind = kind
        self.name = name
        self.age = age
        self.colour = colour

    # Method adding behaviour to class Cat
    # also commonly called a getter
    def meow(self):
        print(f"{self.name} says meow")

    # Give Python a hint on how to print our class
    # this is also commonly called a toString
    def __str__(self):
        return f"The {self.kind} named {self.name} is {self.age} years old and is {self.colour}"

    # Method adding behaviour changing the object
    # also commonly called a setter
    def change_name(self, new_name):
        self.name = new_name

    # Method adding behaviour that creates an additional attribute
    def apply_vaccine(self, vaccine):
        print(f"Applied vaccine {vaccine} to {self.name}")
        self.last_vaccine = vaccine


# Class blueprint for a Tiger
# Inherit from Cat
class Tiger(Cat):
    # If the child class initializes differently, use super() to initialize the base class first
    def __init__(self, name, age, colour, origin):
        super().__init__("tiger", name, age, colour)
        # origin is country of origin
        self.origin = origin

    # Tiger meows differently
    # override method
    def meow(self):
        print(f"{self.name} says grrr")


# Instantiate object Cat
tom = Cat(name="Tom", age=12, colour="Gray")
tom.kind = "bird"  # Should not be allowed
print(tom)
tom.change_name("Garfield")
# tom.apply_vaccine("covid-19")
mike = Tiger(name="Mike", age=10, colour="Orange", origin="Thailand")
print(mike)
mike.meow()

# Made a base class - Pets
class Pets:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method i will override in child class 'getter'
    def pet_sound(self):
        return f"My pet {self.name} makes a funny sound."

    #toString
    def __str__(self):
        return f"I have a pet named {self.name} and they are {self.age}."

    # Method adding behaviour changing the object
    # also commonly called a setter
    def change_name(self):
        self.name = new_name



# Made a child class Dog
class Dog(Pets):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    # new attribute for dog class
    def my_breed(self):
        return f"My pet {self.name} is a {self.breed} breed of dog."

    #over riding the method in the base class
    def pet_sound(self):
        return f"My pet {self.name} makes a woof sound."


@property
# pop = Pets(name = 'Baloo', age = 1)
# print(pop.pet_sound())
Baloo = Dog(name = 'Baloo', age = 1, breed ='labrador')
print(Baloo.pet_sound())

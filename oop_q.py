# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle():
    def __init__(self, max_speed, mileage, name="car"):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name

    def __str__(self):
        return f"The {self.name} has a maximum speed of {self.max_speed} and has {self.mileage} miles."

    def seat_capacity(self, capacity):
        return f"The seating capacity of {self.name} is {capacity}."


my_car = Vehicle(70, 10000)
print(my_car)
print(my_car.seat_capacity(5))




class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage, "Bus")


    
#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity=50)
#
school_bus= Bus(10,200)
print(school_bus)
print(school_bus.seat_capacity(20))





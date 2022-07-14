# Python OOPs Exercise 1: Write a Program to create a class by name Students, and initialize attributes like name,
# age, and grade while creating an object.

class Staff():
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def show_details(self):
        print('Name: {} /n Salary: {} /n Dept: {}'.__format__(self.name, self.salary, self.department))



# class Teacher(Staff):
#     def __init__(self, name, grade):
#         super().__init__(name,grade)

staff_1 = Staff('Hannah', 25000, 'English')
print(staff_1.show_details)
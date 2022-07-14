class Employee:


    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)





emp_1 = Employee('Hannah', 'Whiteley')
emp_1.first = 'Alice'
print(emp_1.first)
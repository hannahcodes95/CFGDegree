#Simple calculator program

def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def division(a,b):
    if b == 0:
        raise ValueError('Can not divide by zero!')
    return a // b

instance = add(10,5)
instance2 = subtract(10,5)

print(f"Result: {instance2}")
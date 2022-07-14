import math

def output_separator(func):
  def inner(*arg):
    print("#" * 30)
    func(*arg)
    print("#" * 30)
  return inner


@output_separator
def square_root(number):
  root = math.sqrt(number)
  print(root)


@output_separator
def square(number):
  squared_number = number * number
  print(squared_number)


@output_separator
def smiley_string(string1, string2):
  print(f"{string1} :)")
  print(f"{string2} :)")


square_root(16)
square_root(9)
square_root(50)
square(2)
smiley_string('Baloo', 'Willow')
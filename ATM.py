# make a dictionary with the pin and balance
import sys

valid_pin = 1234
balance = 1000
max_attempts = 3


# A function for cash withdraw
def withdraw_cash():
    global balance
    amount = int(input("How much would you like to withdraw? "))
    if amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print(f"You now have £{balance} left in your account.")
    return 0

# A function for balance enquiry
def balance_enquiry():
    print(f"Total balance: £{balance}")
    return balance


def authenticate_pin(user_pin=int, valid_pin=int):
    return valid_pin == user_pin


def present_valid_interface():
    quit = False
    while quit == False:
        print("What would you like to do? 1 for cash withdraw, 2 for balance enquiry and 3 to quit.")
        user_choice = int(input("Enter the number you would like: "))
        if user_choice == 1:
            withdraw_cash()
        elif user_choice == 2:
            balance_enquiry()
        elif user_choice == 3:
            print('Program will now quit')
            quit = True
        else:
            print('Invalid input.')
    return 0


''' 
    If attempt count is >= max attempt program exits.
    Ask for new pin attempt. 
    Authenticate that new pin.
    If it is valid present_valid_interface.
    If not valid call the function agaian and increment attempt num by 1.
'''


def present_invalid_interface(local_valid_pin=int, attempt=int):
    if attempt >= max_attempts:
        print('Out of pin attempts. Program will exit.')
        return 1
    else:
        print('Incorrect pin please try again.')

    new_user_pin = int(input("Please enter your pin: "))
    if authenticate_pin(new_user_pin, local_valid_pin):
        present_valid_interface()
    else:
        attempt += 1
        present_invalid_interface(local_valid_pin, attempt)
    return 0

##########################################################################
#Commented out for unit testing, uncomment to enter program.
# user_pin = int(input("Enter four digit pin: "))
# if authenticate_pin(user_pin, valid_pin):
#     present_valid_interface()
# else:
#     present_invalid_interface(valid_pin, 1)

# Test pin authentication with a valid pin, invalid pin and a string.
# authenticate_pin(1234,1234)
# print(authenticate_pin())


# Get pin from user
# Authenticate it
# Present user with ATM options - handle all options
# Exit

# Question 1
# Use the Simple ATM program to write unit tests for your functions.
# You are allowed to re-factor your function to ‘untangle’ some logic into smaller blocks of code to make it easier to write tests.
# Try to write at least 5 unit tests in total covering various cases.



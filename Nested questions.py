# 2D Array Summing
# Create a function that takes in a 2D array (a1), which is populated by arrays of integers. For each array within a1,
# add the greatest integer to a running total, and have the function return that total.
# Example:
# a1 = [[1, 7, 3], [14], [87, 1, 4, 65]]
# returned value = 108 (7 + 14 + 87)
############################

def running_total_greatest_int(array):
    i = 0
    running_total = 0
    while i < len(array[i]):
        j = 0
        while j < len(array[i]):
            print(f"Checking Array j: {array[j]}")
            largest_int = max(array[j])
            running_total += largest_int
            print(f"Largest integer: {largest_int}")
            j +=1
        i +=1
    print(f" Total: {running_total}")
    return running_total


# running_total_greatest_int([[1, 7, 3], [14], [87, 1, 4, 65]])

########################

# Largest Even Number
# Create a function that takes in an array (a1) of integers as an argument, and returns the highest possible even number
# of the sum of any two numbers in the array. You cannot use the same array entry twice to generate this product (i.e.
# you cannot do 3+3 if the a1 array is [3, 1, 0]). Return -1 if no even number sum is found (as would be the case in
# [1, 4])
# Example input and output:
# a1 = [8, 13, 4, 7, 9]
# a2 = 22 (from 13 + 9)

def highest_even_num(array = int):
    i = 0
    even_num = 0
    while i < len(array):
        print(f"Checking Array i: {array[i]}")
        j = 0
        while j < len(array):
            print(f"Checking Array j: {array[j]}")
            sum_of_nums = array[i] + array[j]
            if i != j and sum_of_nums % 2 == 0 and sum_of_nums > even_num:
                even_num = sum_of_nums

            j +=1
        i +=1
    print(f"The highest even number: {even_num}.")
highest_even_num([8, 13, 4, 7, 9])
# I have summed the even numbers in the nested while loop for j. I now need to get all those values and check for the
# max number.


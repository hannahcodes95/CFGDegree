# For any given list of integers, return the first pair of numbers for which their difference is equal to a certain
# number in parameter

# def pair_difference(array, target_num):
#     print('hello')
#     i = 0
#     while i < len(array):
#         print("########################################")
#         print(f"I: {i}, Number:{array[i]}")
#         j = 0
#         while j < len(array):
#             print(f"J: {j}, Number:{array[j]}")
#             if array[i] - array[j] == target_num or array[j] - array[i] == target_num:
#                 print(f"[{array[i]}, {array[j]}]")
#                 return [array[i], array[j]]
#             j+=1
#         i+=1
#
# pair_difference([1,3,7,-10,5,20], 15)
#













#Two Number Sum -22 points(to prepare in advance)
# You will be asked to write a function that will accept an array of numbers and an integer
# representing a target sum.

# If any two numbers from the accepted numbers sum-up to the target sum, then your
# function should return them in an array, in any order.

# If no two numbers sum up to the target sum, the function should return an empty array.

# Note that the target sum has to be obtained by summing two different numbers in the
# array. You cannot add a single integer to itself in order to obtain the target sum.

# Example Input into your function
# my_numbers = [3, 5, -4 ,8, 11, 1, -1, 6] | target_sum = 10

# Example output returned
# [-1, 11] | Numbers can be returned in any order → it does not matter


########################################################


def number_sum(array, target_num):
    i = 0

    while i < len(array):
        print("########################################")
        print(f"I: {i}, Number:{array[i]}")
        j = 0
        while j < len(array):
            print(f"J: {j}, Number:{array[j]}")
            if i != j and array[i] + array[j] == target_num:
                print(f"Found at {array[i]}, {array[j]}.")
                return [array[i], array[j]]
            j += 1
        i += 1
    print("Nothing found")
    return []

number_sum([3, 5, -4 ,8, 11, 1, -1, 6], 10)



#######################################
# def number_sum_triple(array, target_num):
#     i = 0
#
#     while i < len(array):
#         print("########################################")
#         print(f"I: {i}, Number:{array[i]}")
#         j = 0
#         while j < len(array):
#             print(f"J: {j}, Number:{array[j]}")
#             k = 0
#             while k < len(array):
#                 print(f"K: {k}, Number:{array[k]}")
#                 if i != j and i != k and k != j and array[i] + array[j] + array[k] == target_num:
#                     print(f"Found at {array[i]}, {array[j]}, {array[k]}.")
#                     return [array[i], array[j], array[k]]
#                 k+=1
#             j+=1
#         i+=1
#     print("Nothing found")
#     return []
#
# number_sum_triple([3, 5, -4 ,8, 11, 1, -1, 6], 25)
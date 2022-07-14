def square_num(array):
    i = 0
    squared_num = []

    while i < len(array):
        print(f"Checking index : {i} number: {array[i]}")
        squared_num = [(array[i])**2]
        i+=1
        print(squared_num)

    return squared_num


square_num([1,2,3,5,6,8,9])



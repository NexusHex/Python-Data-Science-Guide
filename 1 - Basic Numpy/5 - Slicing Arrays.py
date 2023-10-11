import numpy as np

arr = np.arange(100)

# You can get a certain range of elements from an array by slicing the indexes

arr_get = arr[:10]  # This will get all elements from 0 to the 10th element
print(arr_get)  # Returns a list of elements: [0 1 2 3 4 5 6 7 8 9]
# 10 isn't included because 0 is the first element rather than one

# Trying to change an element in a sliced array...
arr_get[0] = 101
print(arr_get)  # [101 1 2 3 4 5 6 7 8 9]
print(arr)  # [101 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ...]
# Also changes the same element in the original array
# Sliced arrays share the same memory as the original array
# To make a sliced array with a different memory space as the original array, use the .copy() method:
arr_copy = arr[5:20].copy()  # Take all elements from arr from the 5th element to the 20th element
arr_copy[3] = 400
print(arr[7])  # This remains as 8
print(arr_copy[3])  # While this is changed to 400

# You can also slice an array to take in jumps between elements:
arr = np.arange(100)
print(arr[::5])  # This will return all the values in arr with a +5 jump between each element
# Output:
# [0 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95]

# Putting a negative jump will start the sliced array from the end:
print(arr[::-5])
# Output:
# [99 94 89 84 79 74 69 64 59 54 49 44 39 34 29 24 19 14 9 4]
# Note how 100 is not included because 99 is the 100th element. 0 being first makes every element's value = element - 1

# Reversing an array by slicing it:
print(arr[::-1])  # This is just jumping between elements by -1
# Output:
# [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83,
#  82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66,
#  65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49,
#  48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32,
#  31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15,
#  14, 13, 12, 11, 10,  9,  8,  7,  6,  5,  4,  3,  2,  1,  0]

# Accessing a whole row of an array through slicing:
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(arr[1,:])  # Go into index 1 ([4, 5, 6]) and slice everything from that index

# Accessing a whole column of an array through slicing:
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(arr[:,2])  # Slice everything from index 2 of each row (3, 6 and 9)

# Accessing rows and columns in an array through slicing:
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
])
print(arr[0:3, 0:2])  # Go to rows 0-2 (not incl 3), then go to columns 0-1 (not incl 2) - [[1, 2], [4, 5], [7, 8]]
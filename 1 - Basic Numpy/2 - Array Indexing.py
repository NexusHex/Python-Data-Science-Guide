import numpy as np

# Normal indexing of arrays:
one_dim = np.array([1, 2, 3])
i = one_dim[2]  # This is element '3' (3rd element in the 1D array)
print(i)

two_dim = np.array([[1, 2, 3], [4, 5, 6]])
i = two_dim[1][1]  # This is element '5' (2nd 1D array and first element within that 1D array)
print(i)

three_dim = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
i = three_dim[0][1][2]  # This is element '6' (1st 2D array, then 2nd 1D array in 2D array, then 3rd value in 1D array)
print(i)

# Using indexing to take parts of arrays:
arr = np.arange(100)  # Generate an array of values from 0-99
get_arr = arr[arr<=50]  # Put all elements within array 'arr' where the element is less than or equal to 50 (0-50)
print(get_arr)

# Using indexing to take specific segments of lists (two specified ranges):
arr = np.arange(100)
get_arr = arr[(arr<=30) & (arr>=20)]  # Put all elements within array 'arr' where the element is less than or equal to 30 and more than or equal to 20 (basically take all numbers from 20-30)
# Instead of using 'and' like you would most of the time, you need to use the & sign to represent 'and' here. 'and' is used for single values (boolean, integer, string) while & is used for arrays and other multiple-value data (EXCLUDING LISTS, TUPLES, DICTIONARIES, SETS. I think this is just a Numpy thing).
# You have to put the segments into brackets, don't have any idea why lmao
print(get_arr)

# Since the last example used & instead of 'and', here is a list of all the method replacements used for arrays:
# and -> &
# or -> /
# not -> ~

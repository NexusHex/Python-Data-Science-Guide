import numpy as np

# There are two ways to get an exact copy of a Numpy array, and those are to copy or to view the array.
# Copying the array creates a totally new object that owns the data of the array with the same items/elements as the original array.
# Viewing the array does not make the view own the data, and any changes to a view will make changes to the original array.

# Copying an Array:
arr1 = np.array([1,2,3,4,5])
arr1_copy = arr1.copy()
arr1_copy[0] = -1  # This will not affect 'arr1', because 'arr1_copy' is a copy of 'arr1', meaning that it has its own data
print(arr1)
print(arr1_copy)

# Viewing an Array:
arr2 = np.array([6,7,8,9,10])
arr2_view= arr2.view()
arr2_view[0] = 1  # This will affect 'arr2', because 'arr2_view' is a view of 'arr2' and shares the same data with it
print(arr2)
print(arr2_view)
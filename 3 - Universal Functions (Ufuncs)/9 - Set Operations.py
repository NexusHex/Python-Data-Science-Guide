import numpy as np

# A set in math is a group of unique elements. This means that nothing is repeated
# Sets are used in math for operations involving frequent intersection, union and differences

# PART I - CREATING A SET IN NUMPY:
# To create a set in Numpy, you can use the np.unique():

a = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])  # This array has multiple repeating values

b = np.unique(a)  # The np.unique() function removes the recurring values
print(b)

# This would return:
# [1 2 3 4 5 6 7]
# Because those are all the unique values that are different from each other and non-recurring

# PART II - FINDING UNION FROM MULTIPLE ARRAYS:
# The union of multiple sets of numbers are the unique values (non-recurring) that the sets have. This means that all recurring values are removed and
# only the values that appear once are kept.
# You find the union of multiple arrays using the np.union1d() ufunc

c = np.array([1,2,3,4])
d = np.array([3,4,5,6])

print(np.union1d(c,d))

# This would return:
# [1 2 3 4 5 6]
# Because those are the only values that appear once. All the recurring values have been removed from the union.

# PART III - FINDING THE INTERSECTION OF MULTIPLE SETS:
# The intersection is the place where multiple sets share the same number ([1 2 3 4] and [4 5 6 7] have an intersection of [4] because they both have 4 in the
# set)
# To find the intersection of multiple sets, you use the np.intersect1d() ufunc. You also need to specify that the sets you are passing in are unique,
# so you need to set the 'assume_unique' parameter to True:

e = np.array([1,2,3,4])
f = np.array([3,4,5,6])

print(np.intersect1d(e,f, assume_unique=True))  # We tell Numpy that both the sets we are passing into the function are unique and have no repeating values

# This would return:
# [3 4]
# Because 'e' and 'f' both share the numbers 3 and 4

# PART IV.I - FINDING THE DIFFERENCE BETWEEN TWO SETS:
# The difference is the values that ARE in the first set but NOT in the second set:
# [1 2 3 4 5] and [8 7 6 5 4]
# The difference is [1 2 3] because the second and first set share [4 5], but the second set doesn't have [1 2 3] - only the first set has it
# You can find the difference between two sets by using the np.setdiff1d() function. Note that you also have to define the 'assume_unique' parameter,
# like the intersection function, to True so that Numpy knows that your sets are unique:

g = np.array([1,2,3,4])
h = np.array([3,4,5,6])

print(np.setdiff1d(g,h, assume_unique=True))

# This would return:
# [1 2]
# Because [1 2] is only present in the first set, and not the second, while [3 4] is the intersection and [5 6] is only present in the second set

# PART IV.II - FINDING THE SYMMETRICAL DIFFERENCE OF TWO SETS:
# The symmetrical difference between two sets are the values that are not present in both sets (only the ones that can only be found in their own set)
# You can find the symmetrical difference between two sets using the np.setxor1d() function (like the last two functions, make sure to set the
# 'assume_unique' parameter to True so Numpy knows that the two sets are unique):

i = np.array([1,2,3,4])
j = np.array([3,4,5,6])

print(np.setxor1d(i,j, assume_unique=True))

# This would return:
# [1 2 5 6]
# Because [1 2 5 6] are the only numbers that are not shared between both sets - those are [3 4] and are not included in the symmetrical difference

# Well done! You have finished this section of the Numpy tutorial, and can move onto learning new things and using your newfound knowledge on cool
# projects! Good job, and farewell!
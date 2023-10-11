import numpy as np

# The product is another word for multiplication, and finding the product of values in a Numpy array means that you multiply all the values in the
# array together.

# PART I.I - FINDING THE PRODUCT OF A SINGLE ARRAY:
# You can find the product of an array using the np.prod() ufunc and passing in the array that you want to find the product of:

print(np.prod([1,2,3,4]))

# This would return:
# 24
# Because 1 * 2 * 3 * 4 = 24

# PART I.II - FINDING THE PRODUCT OF MULTIPLE ARRAYS:
# Finding the product of multiple arrays is pretty much the same as finding the product of one array, it's just that you have to understand the way Numpy
# finds the product in the fist place:

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

prod = np.prod(a,b)  # Get the product of both 'a' and 'b' together
print(prod)

# This would return:
# 40320
# Because Numpy multiplies all the elements in each array together in the order that they were passed into the np.prod() function
# 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 = 40320

# PART I.III - FINDING THE PRODUCT OF ARRAYS WITH AN AXIS:
# You can use the 'axis' parameter in the np.prod() function to change how your output is given. Passing in two arrays and finding the product of them
# both with axis=1 means that Numpy will figure out the product of each array itself rather than multiplying all the values from every array provided
# together:

c = np.array([1,2,3,4])
d = np.array([5,6,7,8])

prod = np.prod([c,d], axis=1)
print(prod)

# This would return:
# [24 1680]
# Because the product of the first array ('c') is 1 * 2 * 3 * 4 = 24
# And the product of the second array ('d') is 5 * 6 * 7 * 8 = 1680
# Since we told Numpy that we are finding the product using an axis of 1, the elements weren't all multiplied together, and we got a view of the
# products of both arrays.

# PART II - CUMULATIVE PRODUCT:
# A cumulative product means partially taking the product of an array(s)
# Finding the cumulative product of [1 2 3 4] would go like this:
# [1 1*2 1*2*3 1*2*3*4] = [1 2 6 24]
# You can use cumulative products in Numpy using the np.cumprod() ufunc:

print(np.cumprod([5,6,7,8]))

# This would return:
# [5 30 210 1680]
# Because the cumulative product of [5 6 7 8] is:
# [5 5*6 5*6*7 5*6*7*8] = [5 30 210 1680]

# Now that you know how to find the products of arrays using universal functions, you can move onto learning how to find things like the HCF or LCM
# of an array(s) in Lesson 6! See you there!
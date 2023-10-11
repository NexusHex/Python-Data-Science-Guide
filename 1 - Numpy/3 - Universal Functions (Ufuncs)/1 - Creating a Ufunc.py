import numpy as np

# PART I - CREATING A UNIVERSAL FUNCTION:

# To create a universal function with Numpy, you need to create a function that does what you want
# the ufunc to do, and then put that function into the 'frompyfunc()' function.

# 'frompyfunc()' takes 3 parameters:
# function = The function that you want the ufunc to use
# inputs = The number of input arguments required for the ufunc to work
# outputs = The number of vectors that are outputted

# This is how we would create our own ufunc to add three arrays' values together:

def add_arr(x, y, z):  # Take three parameters
    return x+y+z  # And add those three parameters' values together

add_arr = np.frompyfunc(add_arr, 3, 1)  # Create new ufunc that uses the 'add_arr' function, takes 3 iterables and returns one vector

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
c = np.array([11,12,13,14,15])

print(add_arr(a,b,c))

# This would return:
# [18 21 24 27 30]
# Because [(1+6+11), (2+7+12), (3+8+13), (4+9+14), (5+10+15)] is [18, 21, 24, 27, 30]

# PART II - CHECKING THE TYPE OF A UFUNC:

# We can check to see whether a function is a ufunc or not by using type():

print(type(add_arr))  # This will return "<class 'numpy.ufunc'>"

# Now that you can create universal function, you can learn about the ones that Numpy already has pre-ported into the library! Move onto Lesson 2 for ufunc arithmetic!
import numpy as np

# One-Dimensional Arrays

one_dim_array = np.array([1, 2, 3])
# Arrays must contain the same data types for all values
# You only require one list index to access element in a one-dimensional array. You can call it the same way you would a list or tuple:
print(one_dim_array[2])  # <---- Index 2 is element '3'

#----------------------------------------------------------------------------------------------------------------------

# Two-Dimensional Arrays
# A two-dimensional array is made of two different parts within one bigger part (ex: a list within a list, or a tuple within a tuple)
# You can imagine it like this:

#               __________________________
#                    Width               |
#             ___________________        |
#             |                 |        | --------- Rectangle
#             |                 | Height |
#             |_________________|        |
#                                        |
#               __________________________

# The Rectangle is the big part, holding two smaller parts: the Width and the Height. It can be put in a Numpy array like this:
rectangle = np.array([['Width'], ['Height']])


#                        ________Array_________
#                        |                    |
#                        |[0][1][2]  [0][1][2]|
#                        |    |          |    |
#                        |___[0]___  ___[1]___|
#                        ||       |  |       ||
two_dim_array = np.array([[1, 2, 3], [4, 5, 6]])

# To access a certain element in the array, you need to give two list indexes; one for the sub-list and one for the value within the sub-list:
#              two_dim_array[0] - [1, 2, 3]
#                         index -  0  1  2

#              two_dim_array[1] - [4, 5, 6] <-----| List index [1]
#                         index -  0  1  2        |
#                                     ^           |
#              Index [1] in list [1}  |           |
#                                     |           |
# To get element '5':                 |           |
print(two_dim_array[1][1])           #|           |
#                   |  |              |           |
#                   |  |--------------|           |
#                   |-----------------------------|

# You can access the amount of dimensions in an array by using the method x.ndim:
amt_dimensions = two_dim_array.ndim
print(amt_dimensions)  # This would return 2, since there are two lists within the array list

# Note that every part of an array should be the same length. If the first list/tuple is 3 elements long, then all others after that should have the same amount of values.

#----------------------------------------------------------------------------------------------------------------------

# Three-Dimensional Arrays
# Three-dimensional arrays are made of multiple two-dimensional arrays, like how a cube (3D) is made of 6 squares (2D)

#                           ________________________Array_______________________________
#                           | __________[0]___________  ______________[1]_____________ |
#                           | | ___[0]___  ___[1]___ |  | _____[0]____  _____[1]____ | |
#                           | | |       |  |       | |  | |          |  |          | | |
three_dim_array = np.array( [ [ [1, 2, 3], [4, 5, 6] ], [ [-1, -2, -3], [-4, -5, -6] ] ] )
#                                0  1  2    0  1  2         0   1   2     0   1   2

# To access a certain element in the array, you need three indexes; one for the sub-list, one for the sub-sub-list, and one for the element in the sub-sub-list (I'm not illustrating this *sobs* the one above this was hard enough)
# To get element '-3':
print(three_dim_array[1][0][2])
# Thought Process (since I'm NOT about to illustrate that):

# Go into SECOND 2D array (index 1)
# Within that 2D array, go into FIRST 1D array (index 0)
# Within that 1D array, access element index 2 (-3)
# This file is just a dictionary of different things you can do with Numpy arrays/other data
# NOTE: Numpy is referred to as 'np' throughout this file

#-----------------------------------------------------------------------------------------------------------------------

# np.array() - CREATE AN ARRAY (linked to a variable most times)

# Use this to create a new array, which can have as many elements and dimensions as you like + more:
# arr1 = np.array([1, 2, 3]) <- One-dimensional, 3 elements
# arr2 = np.array([[1, 2, 3], [4, 5, 6]]) <- Two-dimensional, 6 elements
# arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[-1, -2, -3], [-4, -5, -6]]]) <- Three-dimensional, 12 elements


#-----------------------------------------------------------------------------------------------------------------------

# arr.ndim - RETURN AMOUNT OF DIMENSIONS IN A NUMPY ARRAY

# The amount of dimensions = The amount of elements within the main element

# [ [//////], [//////] ]
# | | //// |  | //// | |
# | sub-main  sub-main | (This is a two-dimensional array, since there are two one-dimensional arrays in another array)
# |                    |
# --------main----------

# You can check for the amount of dimensions within a Numpy array like this:
# array1 = np.array([1, 2, 3])
# print(array1.ndim)
#
# array2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(array2.ndim)

# The result of this code will be:
# 1
# 2
# This is because the first array is a one-dimensional array, while the second is a two-dimensional one

#-----------------------------------------------------------------------------------------------------------------------

# arr.shape - RETURN TUPLE OF AMOUNT OF SUB-ARRAY TYPES ARE IN AN ARRAY

# If the array called is a three-dimensional array, then x.shape will return the amount of 2D arrays, then the amount of 1D arrays in the 2D arrays, and then the amount of values in each 1D array (there can only be one amount of values in an array):
# array = np.array([[[1, 2, 3], [4, 5, 6]], [[-1, -2, -3], [-4, -5, -6]]])
# print(array.shape)

# The result of this code will be:
# (2, 2, 3)
# This is because there are 2 2D arrays in the 3D array ->  1. [[1, 2, 3], [4, 5, 6]]  2. [[-1, -2, -3], [-4, -5, -6]]
# And there are 2 1D arrays in each 2D array ->  (taking array[0] as example)  1. [1, 2, 3]  2. [4, 5, 6]
# And there are 3 elements in each 1D array -> [1, 2, 3] (3)  [4, 5, 6] (3)  [-1, -2, -3] (3)  [-4, -5, -6] (3)

# You can take certain values from this tuple by specifying an index:
# array = np.array([[[1, 2, 3], [4, 5, 6]], [[-1, -2, -3], [-4, -5, -6]]])
# print(array.shape[0])
# print(array.shape[2])

# The result of this code will be:
# 2
# 3
# This is because the element with index [0] will be the amount of 2D arrays within the 3D array (2), while the element with index [2] will be the amount of elements within each 1D array (3)

#-----------------------------------------------------------------------------------------------------------------------

# arr.size - RETURNS THE TOTAL AMOUNT OF ELEMENTS IN THE WHOLE ARRAY

# You can use this to find the number of elements that a Numpy array holds altogether:
# array = np.array([[[1, 2, 3], [4, 5, 6]], [[-1, -2, -3], [-4, -5, -6]]])
# print(array.size)

# The result of this code will be:
# 12
# This is because each 1D array holds 3 values, and there are 4 1D arrays altogether. 3 * 4 = 12 elements in total

#-----------------------------------------------------------------------------------------------------------------------

# np.arange(arr_min=None, arr_max, num_jump=None) - CREATES A 1D NUMPY ARRAY THAT GOES FROM arr_min TO arr_max - 1 WITH num_jump JUMPS BETWEEN NUMBERS
# If 'arr_min' is not specified, then the array will start from 0 until arr_max - 1
# If 'num_jump' is not specified, then num_jump = 1 (array numbers go up in ones)

# You do not have to specify the start point of your array - this will start the array from 0:
# arr = np.arange(10) <- We only input arr_max
# print(arr)

# The result of this code will be:
# [ 0  1  2  3  4  5  6  7  8  9 ]
# Note that 10 is not included, and you would have to input 11 for the array to include that

# You can also create arrays while specifying arr_min as well as arr_max:
# arr = np.arange(10, 21)
# print(arr)

# The result of this code will be:
# [ 10  11  12  13  14  15  16  17  18  19  20 ]
# We can see that the array didn't start with 0 this time, since we specified arr_min this time.

# You can also make the array take jumps in addition/subtraction for all elements:
# arr = np.arange(4, 31, 2)
# print(arr)

# The result of this code will be:
# [ 4  6  8  10  12  14  16  18  20  22  24  26  28  30 ]
# This is because the array is going from 4 to 30 (31-1) with +2 skips between elements (basically the 2 times-table)

#-----------------------------------------------------------------------------------------------------------------------

# np.random.permutation(arr) - RANDOMLY SHUFFLE ALL THE VALUES WITHIN AN ARRAY

# Use this to shuffle your arrays for when you need random outcomes in your code:
# arr = np.random.permutation(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(arr)

# The result of this code could be something like this:
# [ 7  10  2  6  9  5  3  1  4  8 ]
# This lets you randomize the order of elements in an array

#-----------------------------------------------------------------------------------------------------------------------

# np.random.randint(low, high=None) - RETURNS A RANDOM NUMBER IN THE RANGE BETWEEN low AND high
# If 'high' isn't defined, then the range will be from 0 to 'low'

# Use this method to get a random integer between 0 and a provided number:
# for x in range(10):
#   rand_num = np.random.randint(20)
#   print(rand_num)

# The result of this code may be something like this:
# 9
# 6
# 9
# 14
# 6
# 14
# 0
# 2
# 17
# 14
# All returned values are somewhere between 0 and 20

# You can also use this method to control the range of random numbers chosen by defining a 'high' parameter:
# for x in range(5):
#   rand_num_ctrl = np.random.randint(20, 30)
#   print(rand_num_ctrl)

# The result of this code may be something like this:
# 21
# 25
# 28
# 22
# 24
# All returned values are between 20 and 30

# You can also use it to just generate a single number - just don't put it in a loop:
# rand_num = np.random.randint(10, 20)
# print(rand_num)

# Possible result:
# 17

#-----------------------------------------------------------------------------------------------------------------------

# arr.reshape(height, width) - GIVE A NEW SHAPE TO AN ARRAY WITHOUT CHANGING ITS DATA

# Use this method to take an already created array and convert it to a shape of your liking:
# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# b = a.reshape(2, 5)
# print(b)

# The result of this code would be:
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]
# The arr.reshape method has reshaped the array to look like a 2x5 shape. 2 is the height, while 5 is the width

#-----------------------------------------------------------------------------------------------------------------------

# np.random.rand(height, width) - CREATE AN ARRAY OF RANDOM VALUES FROM 0 TO 1. SHAPE + NUMBER OF ELEMENTS IS DETERMINED BY height AND width

# Use this method to create an array with a certain shape while having random values between 0 and 1:
# arr = np.random.rand(3, 4)
# print(arr)

# Possible result:
# array([[0.31040876, 0.44920803, 0.7009421 , 0.89390266],
#        [0.69538745, 0.89363795, 0.58241282, 0.26536682],
#        [0.6130566 , 0.91968957, 0.10737997, 0.53455056]])
# All elements are between 0 and 1, and the array is shaped to be a 3x4 matrix

# You can create arrays with as many dimensions as you like. The one above was a two-dimensional array. Here is a four-dimensional array:
# arr = np.random.rand(2,3,4,2)
# print(arr)

# Possible result:
# array([[[[0.3728958 , 0.33459857],
#          [0.46422936, 0.54579007],
#          [0.09124789, 0.91793329],
#          [0.72157305, 0.89414614]],
#
#         [[0.29666331, 0.83422357],
#          [0.04055408, 0.44295709],
#          [0.07106515, 0.40883317],
#          [0.72856763, 0.23440019]],
#
#         [[0.61852172, 0.01210622],
#          [0.5484827 , 0.20277045],
#          [0.95418864, 0.77103711],
#          [0.70733567, 0.20932702]]],
#
#
#        [[[0.14159347, 0.06838824],
#          [0.69053491, 0.49880116],
#          [0.20388403, 0.76860325],
#          [0.40990188, 0.96198704]],
#
#         [[0.91286546, 0.68811511],
#          [0.35623622, 0.30603019],
#          [0.50978836, 0.1301417 ],
#          [0.95950479, 0.0910596 ]],
#
#         [[0.85806723, 0.91633391],
#          [0.7005626 , 0.815278  ],
#          [0.01993863, 0.07071634],
#          [0.38103706, 0.3518042 ]]]])
# In the 4D array, there are 2 3D arrays
# In each 3D array, there are 3 2D arrays
# In each 2D array, there are 4 1D arrays
# In each 1D array, there are 2 elements

#-----------------------------------------------------------------------------------------------------------------------

# np.argwhere(arr=elmnt)[idx1][idx2]... - CHECK FOR ALL ELEMENTS THAT ARE SPECIFIED TO SEE IF THEY ARE IN THE MENTIONED arr.
# OUTPUT CAN BE MODIFIED USING idx1, idx2 AND FURTHER INDEX SPECIFIERS DEPENDING ON THE DIMENSIONS OF THE ARRAY

# Use this method to find a certain element's index easily:
# array = np.arange(100)
# get_ind = np.argwhere(array==57)
# print(get_ind)

# The result of the code would be:
# array([[57]], dtype=int32)
# This gets returned because Numpy found the element 57 at index 57 (remember that the array would start with 0 since a minimum value wasn't specified).
# Note how it returns a lot of useless stuff that we don't usually need.

# You can get the result of a certain number and nothing else by specifying an index:
# array = np.arange(100)
# get_ind = np.argwhere(array==44)[0][0]
# print(get_ind)

# The result of the code would be:
# 44
# Note how nothing else got returned, unlike when the method was run without indexes. Specifying an index can save a lot of extra stuff from being outputted.

# But what if multiple of something exists in an array?
# array = np.arange(10)
# array[6] = 5
# get_ind = np.argwhere(array==5)
# print(get_ind)

# The result would be:
# array([[5],
#        [6]], dtype=int32)
# Now both instances of 5 being an element get returned in separate nested lists:
#  [[5], [6]]
# [0][0] [1][0]

# To get both values without the other useless stuff, you can just print it out rather than putting it in a variable - the list is only outputted (convenient ikr):
# array = np.arange(10)
# array[6] = 5
# print(np.argwhere(array==5))

# The result would be:
# [[5]
#  [6]]
# Simple lol, no commas either

#-----------------------------------------------------------------------------------------------------------------------

# np.round(arr, decimals=0) - ROUND THE SPECIFIED ELEMENTS TO THE GIVEN NUMBER OF DECIMALS
# If decimals is not defined, then Numpy will default to 0 decimal points

# To round numbers to the nearest whole number:
# array = np.array([1.34234, 7.562, 14.993])
# rounded_array = np.round(array)
# print(rounded_array)

# The result would be:
# array([ 1.,  8., 15.])
# Every element has been rounded to the nearest whole number, since no decimals parameter has been defined

# To round numbers to 2 decimal points:
# array = np.array([1.3453435, 9.345435345, 8.34545435])
# rounded_array = np.round(array, 2)
# print(rounded_array)

# The result would be:
# array([1.35, 9.35, 8.35])
# All elements have been rounded to 2 decimal places

#-----------------------------------------------------------------------------------------------------------------------

# np.sort(arr, axis=-1) - SORTS AN ARRAY BASED ON THE GIVEN AXIS
# If axis is not defined, then it defaults to -1 (ascending order)

# Sorting a 3D array in ascending order:
# array = np.array([[[3, 1, 2], [6, 5, 4]], [[-2, -3, -1], [-5, -4, -6]]]))
# sorted_array = np.sort(array)

# The result would be:
# array([[[ 1,  2,  3],
#         [ 4,  5,  6]],
#
#        [[-3, -2, -1],
#         [-6, -5, -4]]])
# The array has been sorted in ascending order, without the use of an axis parameter
# If you defined an axis parameter using the maximum dimensions available to sort (2, since the 3rd dimension contains all the 2nd dimensions):
# array = np.array([[[3, 1, 2], [6, 5, 4]], [[-2, -3, -1], [-5, -4, -6]]]))
# sorted_array = np.sort(array, axis=2)

# The result would be the same:
# array([[[ 1,  2,  3],
#         [ 4,  5,  6]],
#
#        [[-3, -2, -1],
#         [-6, -5, -4]]])

# Sorting an array with an axis one less than the maximum dimensions available...
# array = np.sort(np.array([[[3, 1, 2], [6, 5, 4]], [[-2, -3, -1], [-5, -4, -6]]]), axis=1)
# print(array)

# The array will be arranged in descending order:
# Result:
# array([[[ 3,  1,  2],
#         [ 6,  5,  4]],
#
#        [[-5, -4, -6],
#         [-2, -3, -1]]])

# You can also arrange an array in descending order by using np.sort() as well as slicing:
# array = np.sort(np.random.permutation(np.arange(10)))
# array = array[::-1]
# print(array)

# The result would be:
# [9 8 7 6 5 4 3 2 1 0]
# The code sorted a randomly shuffled array of elements from 0-9 in ascending order, then accessed the array using slicing with a step of -1, causing the output to go backwards (aka descending order)

#-----------------------------------------------------------------------------------------------------------------------

# np.hstack((arrs)) - CONCATENATES TWO OR MORE ARRAYS TOGETHER IN A HORIZONTAL FORMAT
# (The arrays must be given in a tuple)
# NOTE: Both arrays must be of the same dimensions (a 3D list can't stack with a 4D list)

# Stacking 2 1D arrays into a horizontally stacked array (sidewards)
# arr1 = np.arange(1, 11)
# arr2 = np.arange(11, 21)
# arr3 = np.hstack((arr1, arr2))
# print(arr1)
# print(arr2)
# print(arr3)

# The result would be:
# [1 2 3 4 5 6 7 8 9 10]
# [11 12 13 14 15 16 17 18 19 20]
# [1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20]
# The two arrays have been stacked horizontally (placed next to each other)

# Stacking 2 2D arrays into a horizontally stacked array:
# arr1 = np.array([[1,2,3],[-1,-2,-3]])
# arr2 = np.array([[4,5,6],[-4,-5,-6]])
# arr3 = np.hstack((arr1, arr2))
# print(arr1)
# print()
# print(arr2)
# print()
# print(arr3)

# The result would be:
# [[ 1  2  3]
#  [-1 -2 -3]]

# [[ 4  5  6]
#  [-4 -5 -6]]

# [[ 1  2  3  4  5  6]
#  [-1 -2 -3 -4 -5 -6]]
# The two arrays have been stacked sidewards (note how the arrays were auto-sorted by Numpy into 3x2 arrays)

#-----------------------------------------------------------------------------------------------------------------------

# np.vstack((arrs)) - CONCATENATES TWO OR MORE ARRAYS TOGETHER IN A VERTICAL FORMAT
# (The arrays must be given in a tuple)
# NOTE: Both arrays must be of the same dimensions (a 3D list can't stack with a 4D list)

# Arranging 2 1D arrays into a vertically stacked array
# arr1 = np.arange(1, 11)
# arr2 = np.arange(11, 21)
# arr3 = np.vstack((arr1, arr2))
# print(arr1)
# print(arr2)
# print()
# print(arr3)

# The result would be:
# [1 2 3 4 5 6 7 8 9 10]
# [11 12 13 14 15 16 17 18 19 20]

# [[1 2 3 4 5 6 7 8 9 10],
# [11 12 13 14 15 16 17 18 19 20]]
# The two arrays have been stacked vertically (note how the two 1D arrays have become a 2D array through being stacked

# Stacking 2 2D arrays in a vertical stack:
# arr1 = np.array([[1,2,3],[4,5,6]])
# arr2 = np.array([[7,8,9],[10,11,12]])
# arr3 = np.vstack((arr1,arr2))
# print(arr1)
# print()
# print(arr2)
# print()
# print(arr3)

# The result would be:
# [[1 2 3]
#  [4 5 6]

# [[7 8 9]
#  [10 11 12]]

# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
# The two arrays have been stacked on top of each other

#-----------------------------------------------------------------------------------------------------------------------


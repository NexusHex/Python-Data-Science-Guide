import numpy as np

# NOTE THAT ALL ARGUMENTS IN THESE FUNCTIONS THAT TAKE THE SHAPE OF THE ARRAY CAN BE HOWEVER BIG YOU LIKE - IT COULD BE A 1D ARRAY OR A 5D ARRAY EVEN.
# I AM SIMPLY USING 2D ARRAYS AT MOST TO KEEP THINGS SIMPLE FOR THE READER

# TYPE 1 - ARRAY OF ZEROS:
# You can make an array with just zeros in them using the np.zeros() function. The number you put in the brackets represents how many 0s are in the array:
zeros = np.zeros(100)  # An array of 100 zeros

# You can also put in array dimensions to make a certain-sized array with a certain amount of numbers:
zeros_with_dims = np.zeros((5, 5))  # This makes a 5x5 array of 0s (You have to put the pair of numbers in another pair of brackets)

# TYPE 2 - ARRAY OF ONES:
# Like an array of 0s, you can make an array of ones using np.ones(). Like np.zeros(), putting one number is the amount of 1s you want in the array,
# and putting a set of dimensions makes an array of 1s shaped like the dimensions you pass into the function:
ones = np.ones(100)  # An array of 100 ones

ones_with_dims = np.ones((5, 2))  # A 5x2 array of ones

# TYPE 3 - FULL ARRAYS:
# You can create arrays full of any number by listing the dimensions of the array and the number that you want the array to be full of in the np.full()
# function:
full = np.full((5, 5), 47)  # A 5x5 array full of 47s

# You can use a previously defined array to determine the shape of a full array, while changing the value that the array will be full of using the full_like() function:
array = np.array([[1,2,3,4,5,6,7,8,9,10], [11,12,13,14,15,16,17,18,19,20], [21,22,23,24,25,26,27,28,29,30], [31,32,33,34,35,36,37,38,39,40]])
array.shape = (2,20)  # Changing the array's shape so it is 2x20

full_from_prev_array = np.full_like(array, 99)  # This will create a full array with the same dimensions as 'array' (2x2) and fill

# TYPE 4 - RANDOM DECIMAL NUMBER ARRAY:
# You can create a randomly generated array with a specified shape that has only decimal numbers between 0 and 1 using the np.random.rand() function:
random = np.random.rand(2,3)  # We create a randomly generated 2x3 array that has decimal numbers between 0 and 1

# TYPE 5 - RANDOM INTEGER ARRAY:
# Create a randomly generated array of integer(s) using the np.random.randint() function
# You specify the start value - where the random selection will start from (if this isn't defined, it is set to 0)
# The end value - where the random selection ends (this is the only required argument to fulfill for randint() to work)
# And the shape of the array - the shape will influence how many values are created and stored into one array

# Random choices are made between the start and end point. If the start point was 5 and the end point was 11, then the random selection would be between 5 and 10 (because indexes are counted starting with 0 instead of 1)
# If the start point was not specified but only the end point was (say that the end point was 11), then the random selection would be between 0 and 10 (because indexes start from 0 instead of 1):
random_ints = np.random.randint(5,11)  # This returns a random integer between 5 and 10

# If you want to generate multiple random integers, then you can set the 'size' argument to incorporate the dimensions of the array
# Say we wanted to have a 5x5 array of random integers between 1 and 50:
random_ints_5x5 = np.random.randint(1,51, size=(5,5))  # Create a 5x5 array with random integers between 1 and 50

# TYPE 6 - IDENTITY ARRAY:
# Identity arrays are square arrays that have a 1 going down the main diagonal and are created using the np.identity() function as well as specifying the dimensions of the array
# (you only need to specify one number, since it's a square array and both sides are the same length):
identity = np.identity(5)  # A 5x5 array with 1 going down the main diagonal line

# It looks like this:
# [[1., 0., 0., 0., 0.],
#  [0., 1., 0., 0., 0.],
#  [0., 0., 1., 0., 0.],
#  [0., 0., 0., 1., 0.],
#  [0., 0., 0., 0., 1.]]
# You can see that there is 1 going down diagonally and the rest of the numbers are 0. You can also see that the array is a 5x5 one



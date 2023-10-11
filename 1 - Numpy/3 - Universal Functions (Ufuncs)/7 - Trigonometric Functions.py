import numpy as np

# Numpy offers ufuncs that take in numbers as radians and return them in their corresponding sin, cos and tan forms.
# Note: I will not be showing the values that get returned, since they are too small or the decimals are too long for them to be efficient.

# PART I.I - TRIGONOMETRIC FUNCTIONS:
# You can use the np.sin(), np.cos() and np.tan() ufuncs to find the sin, cos and tan numbers of the radian that is passed in:
# Note: You can also use the function np.pi() to represent pi

print(np.sin(np.pi/2))
print(np.cos(np.pi/2))
print(np.tan(np.pi/2))

# PART I.II - TRIGONOMETRY ON ARRAYS:
# To calculate trigonometric values from arrays, you just need to pass in the array as normal:

a = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

print(np.sin(a))  # Find the sine of all the values within the array 'a'

# PART II.I - CONVERTING RADIANS TO DEGREES:
# To convert a radian number to degrees, you can use the np.rad2deg() ufunc:

b = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

print(np.rad2deg(b))  # Turn all values in array 'b' from radians to degrees and print them out

# PART II.II - CONVERTING DEGREES TO RADIANS:
# To convert a degree number to radians, you can use the np.deg2rad() ufunc:

c = np.array([90, 180, 270, 360])

print(np.deg2rad(c))  # Turn all values in array 'c' from degrees to radian values
# Note: Formula to calculate radian values from degrees is pi/180 * degree_val

# PART III.I - FINDING ANGLES:
# To find the angles from sin, cos and tan values (AKA inverse sin, cos, tan - arcsin, arccos, arctan) use the np.arcsin(), np.arccos() and np.arctan()
# ufuncs:

print(np.arcsin(1.0))

# PART III.II - FINDING ANGLES OF EACH VALUE IN AN ARRAY:
# Finding the inverse trigonometric value of angles from an arrays is pretty much the same as doing it for one value; just pass in the whole array:

d = np.array([1, -1, 0.1])

print(np.arccos(d))

# PART IV - FINDING HYPOTENUSES:
# Using Pythagoras' Theorem, we can give Numpy the base and perpendicular lengths of a triangle and let Numpy find out the value of the hypotenuse using
# the np.hypot() ufunc:
# Note: Pythagoras' Theorem = a^2 + b^2 = c^2
#    |\
#    | \
# a^2|  \ c^2
#    |___\
#     b^2

base = 3
perpendicular = 4

print(np.hypot(base, perpendicular))  # Calculate the length of the hypotenuse using the lengths of the base and the perpendicular lengths

# This would return:
# 5
# Because Pythagoras' Theorem = a^2 + b^2 = c^2
# 3^2 + 4^2 = 9 + 16 = 25
# 25 = c^2
# √25 = 5
# Hypotenuse length = 5

# Now that you know how to manipulate trigonometric functions using Numpy, you can move onto learning about hyperbolic universal functions in Lesson 8!
# See you there!
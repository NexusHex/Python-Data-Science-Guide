import numpy as np

# There are multiple ways to round decimals from an array using the universal functions that Numpy provides

# PART I - TRUNCATION:
# Truncating a number is, simply, chopping off the decimal part of a number and only leaving the integer. You can truncate an array using the np.trunc()
# ufunc or the np.fix() ufunc (they both do the same thing):

a = np.trunc([-3.1666, 3.6667])
print(a)

# This would return:
# [-3, 3]
# Because truncating a number takes all the decimal values away from it

print(np.fix([-3.1666, 3.6667]))
# Returns the same as above

# PART II - ROUNDING:
# Rounding involves bringing a place value up or down by 1 depending on whether the next place value over is >5 or <5. If the place value is >5, then
# the number is rounded up by 1. If the place value is <5, then the number is rounded down by 1.
# Use the np.around() ufunc to round values based on the amount of decimal places you would like to keep (how many numbers after the decimal point are
# shown):

print(np.around(3.1666, 2))  # Round 3.1666 to 2 decimal places (hundredths)

# This would return:
# 3.17
# Because...
# 3 . 1  6 6
# U . t  h th
# The 6 in the thousandths (th) place is more than 5, so we round the 6 in the hundredths (h) place up by one. 6+1=7, so the rounded number is 3.17

# PART III - FLOOR:
# You can use the np.floor() ufunc to floor the value(s) provided; this means that they are all rounded down to the nearest lower integer (3.6 would
# become 3):

print(np.floor([-3.1666, 3.6667]))

# This would return:
# [-4 3]
# Because the first value is negative, so the nearest lower value is -3-1=-4
# And because the nearest lower integer to 3.6667 is 3

# PART IV - CEIL:
# The np.ceil() ufunc is the total opposite of the np.floor() ufunc, since it rounds the value(s) provided to the nearest upper integer (5.1 becomes 6)

print(np.ceil([-3.1666, 3.6667]))

# This would return:
# [-3 4]
# Because the first value is negative, so the nearest higher value is -3.1666--0.1666=-3
# And because the nearest upper integer to 3.6667 is 4, naturally

# Now that you are proficient in rounding decimals using Numpy and its universal functions, move
# onto Lesson 4 to learn more about summations!
import numpy as np

# Summations are the sum of every value(s) specified, returned in one 1D array
# It is similar to addition, but different, since the 'add()' function lacks the ability to use more than two values/arrays.
# Summations can be done on as many arrays as you like, and it will the sum for each value in a 1D array.

# PART I.I - CREATING A SUMMATION:
# We use the np.sum() ufunc to do summation for us:

a = np.array([1,2,3])
b = np.array([1,2,3])

print(np.sum(a,b))

# This would return:
# 12
# Because (1+2+3=6) + (1+2+3=6) = 12

# PART I.II - SUMMATION OVER AN AXIS:
# If you want the summations of each array then you can specify an axis that Numpy will work on when it is run:

c = np.array([1,2,3])
d = np.array([1,2,3])

print(np.sum([c,d], axis=1))  # You can see that we have had to put in all our parameters that weren't the axis into their own list of parameters, and then specify the 'axis' parameter

# This would return:
# [6 6]
# Because the summation of the first array is 1 + 2 + 3 = 6, and it is the same set of numbers for both, both the summations will have the same result

# PART II - CUMULATIVE SUM:
# A cumulative sum is the partial addition of all the elements in an array
# The cumulative sum of [1 2 3 4 5] would be [1 1+2 1+2+3 1+2+3+4 1+2+3+4+5] or [1 3 6 10 15]
# You can perform cumulative sums using the np.cumsum() function:

print(np.cumsum([1,2,3,4,5]))

# This would return:
# [1 3 6 10 15]
# Because the cumulative sum of [1 2 3 4 5] is [1 1+2 1+2+3 1+2+3+4 1+2+3+4+5], becoming [1 3 6 10 15]

# PART III.I - DISCRETE DIFFERENCES:
# A discrete difference means subtracting two successive elements:
# For [1 2 3 4], the difference would be [2-1 3-2 4-3] = [1 1 1]
# To utilize this, we can use the np.diff() ufunc:

print(np.diff([10, 15, 25, 5]))

# This would return:
# [5 10 -20]
# Because [10, 15, 25, 5] becomes [15-10 25-15 5-25] = [5 10 -20]

# PART III.II - PERFORMING DISCRETE DIFFERENCES REPEATEDLY:
# We can repeatedly use the np.diff() ufunc to find the discrete difference of an array's values by applying the same rules to the result of the previous
# iteration. This can be done by changing a parameter in the np.diff() function called 'n', which represents how many times the discrete difference is
# happening (the default is 1 if you do not define it yourself).

# If you wanted to find the discrete differences in the array [1 2 3 4] with n=2, then you would go as normal - [2-1 3-2 4-3] = [1 1 1] - and then do the
# same thing to the result of the first iteration - [1-1 1-1] = [0 0]

print(np.diff([10, 15, 25, 5], n=2))

# This would return:
# [5 -30]
# Because [15-10 25-15 5-25] = [5 10 -20]
# And [10-5 -20-10] = [5 -30]
# Leaving us with our answer :)

# Now that you can manipulate Numpy to do summations and subtraction, you can move onto using multiplication with the universal functions! See you in
# Lesson 5!
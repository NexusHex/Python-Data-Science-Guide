import numpy as np

# The LCM (Lowest Common Multiple) of a number/group of numbers is the nearest number to all numbers in the set that is a multiple of all the numbers
# in the set:
# The LCM of 1, 2 and 3 is 6, because 1*6=6, 2*3=6, and 3*2=6. It is the closest number to 1,2 and 3 that is a multiple of all three of them

# The HCF (Highest Common Factor, AKA GCD - Greatest Common Denominator) is the biggest number that goes into all the numbers within a group:
# The HCF of 36 and 24 is 12, because 36 goes into 1,2,3,4,6,12,18 and 36, while 24 goes into 1,2,3,4,6,8,12 and 24. If you check both lists of factors...
# 1 2 3 4 6   12 18   36  -  36
# 1 2 3 4 6 8 12   24     -  24
# You'll see that the largest number that both lists of factors have is 12, so the HCF is 12

# PART I.I - FINDING LCM OF TWO VALUES:
# To find the LCM of two values, you can use the np.lcm() ufunc and pass in the array you want to find the LCM of:

a = 4
b = 6

print(np.lcm(a,b))

# This would return:
# 12
# Because that is the lowest number that 4 and 6 have as a multiple (4*3=12, 6*2=12)

# PART I.II - FINDING THE LCM OF AN ARRAY:
# Finding the LCM of a whole array is slightly different to finding the LCM of two different values, since you have to add a new function to the np.lcm()
# ufunc called np.lcm.reduce() - this function uses the np.lcm() function on each element and reduces the array by one dimension, so you just have one
# value (since a 1D array of numbers reduced by a dimension becomes just one value):

c = np.array([3,6,9])

print(np.lcm.reduce(c))  # Finding the LCM of all three numbers

# This would return:
# 18
# Because 18 is the lowest multiple of 3, 6 and 9 (3*6=18, 6*3=18, 9*2=18)

# You can also use this knowledge of finding the LCM of an array to find the LCM of something like a range of values:

d = np.arange(1,11)  # Array with numbers ranging from 1 to 10

print(np.lcm.reduce(d))  # Find the LCM of [1 2 3 4 5 6 7 8 9 10]

# This would return:
# 2520

# PART II.I - FINDING THE HCF (GCD) OF TWO VALUES:
# To find the HCF of two values using Numpy, we use the np.gcd() ufunc and pass in the values that we want to find the HCF of:
# Note: I know that I've been calling it the HCF, but Numpy calls it the GCD, so the ufunc takes GCD instead of HCF.

e = 6
f = 9

print(np.gcd(e,f))  # Find the HCF of 6 and 9

# This would return:
# 3
# Because that is the highest number that goes into both 6 and 9:
# 1 2 3 6  -  6
# 1   3 9    -  9
#    ___

# PART II.II - FINDING THE HCF (GCD) OF AN ARRAY:
# Finding the HCF of all the values in an array works the same as finding the LCM of all the values in an array - the np.gcd.reduce() ufunc:

g = np.array([20, 8, 32, 36, 16])

print(np.gcd.reduce(g))  # Find the HCF of all the values within 'g'

# This would return:
# 4
# Because it is the largest number that you can divide all the values by (20/5=4, 8/2=4, 32/8=4, 36/9=4, 16/4=4)

# Now that you can find the LCM of HCF of values or arrays, you can move onto learning about some of the trigonometric functions that Numpy offers with
# its ufuncs! See you in Lesson 7!
import numpy as np

# Some of the functions available from the universal functions are ones surrounding basic arithmetic, like adding, subtracting, multiplying and dividing
# Like explained in Lesson 0, using a ufunc is much faster than the standard methods available from base Python, so we should use these functions to
# boost our program speed

# PART I - ADDITION:
# To add the values of different arrays together, we use the np.add() ufunc to add the values to each other:

a = np.array([10, 11, 12, 13, 14, 15])
b = np.array([20, 21, 22, 23, 24, 25])

c = np.add(a,b)
print(c)

# This will return:
# [30 32 34 36 38 40]
# Because [(10+20), (11+21), (12+22), (13+23), (14+24), (15+25)] becomes [30,32,34,36,38,40]

# PART II - SUBTRACTION:
# To subtract the values of different arrays from one another, we use the np.subtract() ufunc:

d = np.array([10, 20, 30, 40, 50, 60])
e = np.array([20, 21, 22, 23, 24, 25])

f = np.subtract(d,e)
print(f)

# This will return:
# [-10 -1 8 17 26 35]
# Because [(10-20), (20-21), (30-22), (40-23), (50-24), (60-25)] becomes [-10 -1 8 17 26 35]

# PART III - MULTIPLICATION:
# To multiply the values of different arrays with each other, we use the np.multiply() ufunc:

g = np.array([10, 20, 30, 40, 50, 60])
h = np.array([20, 21, 22, 23, 24, 25])

i = np.multiply(g,h)
print(i)

# This will return:
# [200 420 660 920 1200 1500]
# Because [(10*20), (20*21), (30*22), (40*23), (50*24), (60*25)] becomes [10, 20, 30, 40, 50, 60]

# PART IV - DIVISION:
# To divide the values of different arrays by each other, we use the np.divide() ufunc:

j = np.array([10, 20, 30, 40, 50, 60])
k = np.array([3, 5, 10, 8, 2, 33])

l = np.divide(j,k)
print(l)

# This will return:
# [3.33333333 4. 3. 5. 25. 1.81818182]
# Because [(10/3), (20/5), (30/10), (40/8), (50/2), (60/33)] becomes [3.33333333, 4., 3. 5. 25. 1.81818182]
# Note that when one value is a float, all the other values in the array become floats; this is because all values within an array must have the same type
# If you tried to see the 'dtype' of the 'l' array, it would be 'float64', since all the values are floats

# PART V - POWERS:
# To raise the first passed array by the second passed array, we use the np.power() ufunc:

m = np.array([10, 20, 30, 40, 50, 60])
n = np.array([3, 5, 6, 8, 2, 33])

o = np.power(m,n)
print(o)

# This will return:
# [1000 3200000 729000000 6553600000000 2500 0]
# Because [(10^3), (20^5), (30^6), (40^8), (50^2), (60^33)] becomes [1000 3200000 729000000 6553600000000 2500 0]
# Note that Numpy changes the last value to 0. This is because the value is too long for the program to show (60^33 = 4.77519666596 E58)

# PART VI - REMAINDERS:
# To get the remainders after dividing the arrays provided, you can either use the np.mod() ufunc or the np.remainder() ufunc - both do the same thing:

p = np.array([10, 20, 30, 40, 50, 60])
q = np.array([3, 7, 9, 8, 2, 33])

# These are both the same thing
r = np.mod(p,q)
s = np.remainder(p,q)
print(r)
print(s)

# This will return: (ignoring the duplicate vector printed out)
# [1 6 3 0 0 27]
# This is because [(10%3), (20%7), (30%9), (40%8), (50%2), (60%33)] becomes [1 6 3 0 0 27]
# 10%3 = 1 because 10 goes into 3 three times (3*3=9) and 10-9=1, so 1 is the remainder

# PART VII - DIVISION + REMAINDER:
# You can use the divmod() function to get both the quotient of the ufunc and the remainder (this comes in two separate arrays):

t = np.array([10, 20, 30, 40, 50, 60])
u = np.array([3, 7, 9, 8, 2, 33])

v = np.divmod(t,u)
print(v)

# This will return:
# (array([3, 2, 3, 5, 25, 1]), array([1, 6, 3, 0, 0, 27]))
# The first array is the array of quotients, and the second is the array of remainders
# Note that the array of quotients is rounded to the nearest integer

# PART VIII - ABSOLUTE VALUES:
# You can get the absolute values from an array by using the abs() or absolute() ufunc:

w = np.array([-1, -2, 1, 2, 3, -4])

x = np.abs(w)
print(x)

# This would return:
# [1 2 1 2 3 4]
# Because the absolute value of a number is the distance it has from 0. The distance from -1 to 0 is +1, so -1 becomes 1 when we apply the abs()
# function to it.

# Now that you know how to use Numpy universal functions to do basic arithmetic, you can now move onto learning how to round numbers! See you in
# Lesson 3!
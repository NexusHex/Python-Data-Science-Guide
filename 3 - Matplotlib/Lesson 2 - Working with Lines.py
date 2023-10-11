import numpy as np
import matplotlib.pyplot as plt

# In this lesson, we will focus on working with Matplotlib's diagram lines, and doing things like customizing certain aspects of them and working with multiple lines

# PART I - LINE STYLE:
# As you learned in Lesson 1, you can edit the line type within the 'fmt' parameter of Matplotlib's plot() function, but plot() also offers a more explicit way to define just the style of line we want to use, in case we don't want to define any of the other two paremters:
y_points = np.array([3, 8, 1, 10])

plt.plot(y_points, linestyle='dotted')  # You can change the style of line that you use using the 'linestyle' parameter (shortened to ls)
plt.show()

# We can also use the 'linestyle' parameter to create a dashed line:
plt.plot(y_points, linestyle='dashed')
plt.show()

# You can also use short terms to define your linestyle, saving you some time:
# linestyle -> ls
# 'dotted' -> ':'
# 'dashed' -> '--'
plt.plot(y_points, ls='--')  # Creating a dashed linestyle using short terms
plt.show()

# You can choose from these styles of lines:
# NOTE: Copied from w3school's Matplotlib tutorial (https://www.w3schools.com/python/matplotlib_line.asp)
# '-' or 'solid' = Solid Line (default)
# ':' or 'dotted' = Dotted Line
# '--' or 'dashed' = Dashed Line
# '-.' or 'dashdot' = Dashed + Dotted Line
# 'None' or '' or "" = No line

# PART II - LINE COLOR:
# You can set the color of the line using the 'color' parameter in the plot() function:
# These use the same set of accepted colors as the colors used for the 'fmt' parameter
y_points = np.array([3, 8, 1, 10])

plt.plot(y_points, color = 'r')  # A red line (you can use the shorter 'c' to define the line color value)
plt.show()

# You can also use hexadecimal values or any of the universally accepted color names (https://www.w3schools.com/colors/colors_names.asp)

# PART III - LINE WIDTH:
# You can change the parameter 'linewidth' (short form is 'lw') to affect the width of the line. It is a floating point number:
y_points = np.array([3, 8, 1, 10])

plt.plot(y_points, lw=20.5)
plt.show()

# PART IV - PLOTTING MULTIPLE LINES:
# It's pretty simple to plot more than one line in Matplotlib; you simply have to use the plot() function on all the lines:
y1 = np.array([2, 4, 3, 4, 6])
y2 = np.array([7, 6, 9, 3, 5])

plt.plot(y1)
plt.plot(y2)
plt.show()
# If you run the program, you will realize that the second line automatically gets a new color so that you don't get confused with another line

# You can do the same thing by putting all the values that you need to plot into one plot() function:
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1,y1,x2,y2)  # Plotting the x and y coordinates of both lines
plt.show()

# You can create as many lines as you want, so go wild!
y1 = np.array([2, 4, 3, 4, 6])
y2 = np.array([7, 6, 9, 3, 5])
y3 = np.array([3, 8, 1, 10])
y4 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)
plt.plot(y3)
plt.plot(y4)
plt.show()
# Unfortunately, mashing lots of coordinates together confuses Matplotlib and makes it think that the first value is the array of x values, which will mess up your visualization

# Well done on learning how to customize and plot multiple lines! Move onto Lesson 3 to learn more about Graph Labels!
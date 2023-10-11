import numpy as np
import matplotlib.pyplot as plt

# Matplotlib has a function called plot(), which allows you to draw points in a diagram. It defaults to drawing a line from point to point, so you would have to tell Matplotlib the type of line you want if you wanted, say, a bell curve line
# The plot() function takes two parameters: one for the points on the x-axis (horizontal), and the other for the points on the y-axis (vertical)
# We can use an array-handling tool like Numpy to create arrays containing all the points that we need to put into the plot() function's parameters! Say we needed to plot a straight line between coordinates (1,3) and (8,10)...

# PART I - PLOTTING A LINE BETWEEN TWO POINTS:
x_points = np.array([1, 8])  # We create a Numpy array storing all the points we need on the x-axis (we are going from x coordinate 1 to 8)
y_points = np.array([3, 10])  # And we create another Numpy array to store all the points we need on the y-axis! (we are going from y coordinate 3 to 10)

# If you don't understand what just happened, then check this out!
# We are going from:
# (  1    ,    3  )
#    |         |
# x_points  y_points
#    |         |
# (  8    ,   10  )
# So we take the range of where we want to go on each axis and put it in its respective Numpy array!

# Now that we have defined our points for the diagram line, we can plot them using Matplotlib!
plt.plot(x_points, y_points)
plt.show()  # show() is basically Matplotlib's way of saying 'print(the_plotted_data_!)'

# PART II - PLOTTING TWO POINTS WITHOUT A LINE IN-BETWEEN:
# If we just want Matplotlib to plot two points, but not plot a line between the points, then we simply have to give the plot() function another parameter to work with!
# We will use the parameter shortcut 'o', meaning rings, to tell Matplotlib that we just want the points (rings) to be visible and not the line:

x_points = np.array([1, 8])
y_points = np.array([3, 10])

plt.plot(x_points, y_points, 'o')  # We add a new parameter to the end of the plot function, telling Matplotlib that we just want the rings/points to be shown
plt.show()

# PART III - PLOTTING MULTIPLE POINTS:
# If you want to plot more than two points, then that's totally possible! The only thing you have to make sure of is that both the x and y points have the same amount of points specified, otherwise Matplotlib will have either too many or too little points than it knows what to do with!

x_points = np.array([1, 2, 3, 4])
y_points = np.array([1, 5, 3, 7])

plt.plot(x_points, y_points)
plt.show()

# PART III.I - WHAT IF YOU DON'T SPECIFY THE X VALUE?:
# If you do not specify the x points for Matplotlib to plot, then Matplotlib will default to setting the x values in numerical order (0, 1, 2, 3...). This can be useful to save time when your data has a new entry on every single new x line:
y_points = np.array([3, 5, 2, 6, 8, 4, 6])

plt.plot(y_points)
plt.show()
# Since there were 7 values in the y_points array, the x-axis goes from 0 to 6

# PART IV - PLOTTING POINTS WITH MARKERS:
# By default, Matplotlib draws your plotted data as a line between specified points, but what if you want those points to be easy to see?
# Like just having the points shown and not the line, we simply need to add another parameter to the plot() function to tell Matplotlib that we want the points to be marked out clearly; it is called the 'marker' parameter:
y_points = np.array([3, 5, 2, 6, 8, 4, 6])

plt.plot(y_points, marker='o')  # We specify the 'marker' parameter and set it to 'o' (remember how we set the dots without the line to 'o' as well? This is so that the points are shown as circles/rings)
plt.show()

# PART IV.I - OTHER MARKERS:
# Valid marker values:
# NOTE: Copied from w3school's Matplotlib tutorial (https://www.w3schools.com/python/matplotlib_markers.asp)
# 'o' = Circle
# '*' = Star
# '.' = Point
# ',' = Pixel
# 'x' = X
# 'X' = X (filled)
# '+' = Plus
# 'p' = Plus (filled)
# 's' = Square
# 'D' = Diamond
# 'd' = Diamond (thin)
# 'p' = Pentagon
# 'h' = Hexagon
# 'H' = Hexagon (filled)
# 'v' = Triangle Facing Down
# '^' = Triangle Facing Up
# '<' = Triangle Facing Left
# '>' = Triangle Facing Right
# '|' = Vertical Line
# '_' = Horizontal Line

# PART IV.II - FORMATTING LINES AND POINTS:
# The parameter we have been using to define the type of marker we have is called 'fmt', meaning format, and we can change other aspects of this parameter to change things like the line type and the color of the line.
# The 'fmt' parameter's order of defining markers, line types and line/marker colors is like this:
# marker|line_type|color (no spaces between parameters)

# Valid line parameter values:
# NOTE: Copied from w3school's Matplotlib tutorial (https://www.w3schools.com/python/matplotlib_markers.asp)
# '-' = Solid Line
# ':' = Dotted Line
# '--' = Dashed Line
# '-.' = Dashed + Dotted Line
# Note that leaving out the line option in the 'fmt' parameter will default to there being no line

# Valid color parameter values:
# NOTE: Copied from w3school's Matplotlib tutorial (https://www.w3schools.com/python/matplotlib_markers.asp)
# 'r' = Red
# 'g' = Green
# 'b' = Blue
# 'c' = Cyan
# 'm' = Magenta
# 'y' = Yellow
# 'k' = Black
# 'w' = White

# PART IV.III - CHOOSING MARKER SIZE:
# You can change the parameter 'markersize' in the plot() function to change the size of the marker in pixels (shorter version is ms):
y_points = np.array([3, 5, 2, 6, 8, 4, 6])

plt.plot(y_points, 'D:g', markersize=20)  # Plotting points on a diagram with diamond markers, dotted lines and green color with a marker size of 20 pixels
plt.show()

# PART IV.IV - CHOOSING A MARKER OUTLINE AND FACE COLOR:
# If you want your markers to have a colored outline that is different to the primary color of the marker, then you can customize it to look like that using the 'markeredgecolor' parameter in the plot() function (or the shorter mec):
y_points = np.array([3, 5, 2, 6, 8, 4, 6])

plt.plot(y_points, 'D:g', markersize=20, markeredgecolor='r')  # Diamond markers, dotted lines, green color, marker size of 20 pixels, red marker frame (you can use the same short notation that you use for the 'fmt' parameter to choose the color)
plt.show()

# If you want the primary color of your marker to be different to the color of the line, then you can also customize that using the 'markerfacecolor' parameter in the plot() function (short form is mfc):
y_points = np.array([3, 5, 2, 6, 8, 4, 6])

plt.plot(y_points, 'D:g', markersize=20, markeredgecolor='r', markerfacecolor='m')  # Diamond markers, dotted lines, green color, marker size of 20 pixels, red marker frame, magenta marker face
plt.show()

# If you want to color the entire marker one color, then just use the 'mec' and 'mfc' parameters together with the same color:
y_points = np.array([1, 3, 2, 5, 3, 8])

plt.plot(y_points, marker='*', ms=20, mec='r', mfc='r')  # Star marker, 20-pixel size marker, red edge color, red face color
plt.show()

# Note that you can also use hexadecimal color values to determine the color of a marker...
# Or any of the 140 universally supported color names (https://www.w3schools.com/colors/colors_names.asp)

# Now that you know how to plot and customize your points, you can move onto working with different kinds of lines! See you in Lesson 2...
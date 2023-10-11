import numpy as np
import matplotlib.pyplot as plt

# Sometimes, we want to make it easier for a person viewing our data to know exactly where a certain point on one of our lines is, so we may want to add grid lines to make it easier to find!

# PART I - ADDING GRID LINES TO A PLOT:
# It's pretty simple to add grid lines to a plotted graph... you just have to add an extra function before you show() it!
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calories Burned")

plt.plot(x, y)

plt.grid()

plt.show()

# PART II - SPECIFYING WHICH LINES TO DISPLAY:
# If you just want to show grid lines on the x-axis or the y-axis, then you can do that within the grid() function by defining the 'axis' parameter:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calories Burned")

plt.plot(x, y)

plt.grid(axis='x')

plt.show()
# You can edit the 'axis' parameter to show the y-axis grid lines as well, and define the parameter as 'both' to show both grid lines on both axes.
# If you call grid() without defining the 'axis' parameter, the default value of 'axis' is 'both'

# PART III - SETTING LINE PROPERTIES FOR THE GRID LINES:
# Matplotlib lets you customize aspects of the grid lines, like the color, line style and line width inside of the grid() function
# This uses the parameters 'color', 'linestyle' and 'linewidth':
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calories Burned")

plt.plot(x, y)

plt.grid(color='green', linestyle='--', linewidth=0.5)  # You can use the same short form names and short notation as before (like how '--' means 'dotted')

plt.show()

# PART IV - PUTTING GRID LINES BEHIND A GRAPH:
# Sometimes when using subplots, the grid lines will overlap with the items in the area covered by the grid lines, making the graph look unclean and unconventional
# We can change this and make sure that the lines don't overlap by changing a value of the plot we create: set_axisbelow():
# (this is clearest to see when using bar graphs, so I will use them)

#Note: you will learn more on subplots in the next lesson, and bar graphs in Lesson 6. This is just for reference once you better understand subplots and bar graphs

x = np.array(['A','B','C','D','E','F','G','H','I','J'])
y = np.array([7,3,7,2,1,8,3,6,9,2])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

plt.title('Grid Lines Overlapping the Data (very bad!)')

ax.bar(x,y)
ax.grid(color='red')
ax.set_axisbelow(False)  # Since this is set to False, the grid lines will overlap over the plot

plt.show()
# You will see that the grid is overlapping over the bars, and we don't want that to happen, so we can change the 'set_axisbelow()' value to True
# Note: set_axisbelow() is set to False by default

x = np.array(['A','B','C','D','E','F','G','H','I','J'])
y = np.array([7,3,7,2,1,8,3,6,9,2])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

plt.title('Grid Lines Not Overlapping Over Data (good!)')

ax.bar(x,y)
ax.grid(color='red')
ax.set_axisbelow(True)  # Now that this is set to True, the grid lines will no longer overlap over the data plotted

plt.show()

# You have learned how to add grid lines to your visualized data, and you have also learned how to customize them to your liking. Move onto Lesson 5 to learn some more!
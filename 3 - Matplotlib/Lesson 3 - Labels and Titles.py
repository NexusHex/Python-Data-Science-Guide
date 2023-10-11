import numpy as np
import matplotlib.pyplot as plt

# In this lesson, we will learn about how Matplotlib allows you to customize how you label your graph with axis labels and titles

# PART I - AXIS LABELS:
# If you want to add labels to the x and y axes, we can use the functions 'xlabel()' and 'ylabel()' to change that!
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calories Burned")

plt.show()
# These labels can be whatever you like!

# PART II - GRAPH TITLES:
# Titles can be added to graphs using the 'title()' function (we will use the same plot as above for consistency):
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calories Burned")
plt.title('Sports Watch Data')  # We add a title to the graph called 'Sports Watch Data'

plt.show()
# The title can also be whatever you like!

# PART III - FONT OPTIONS FOR LABELS AND TITLES:
# You can use the 'fontdict' parameter in the 'title()', 'xlabel()' and 'ylabel()' functions to change the font aspects of the title/label:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse", fontdict={'family':'serif','color':'darkred','size':15})  # You use a dictionary to define all the values that you would like for the label/title to have
plt.ylabel("Calories Burned", fontdict={'family':'serif','color':'darkred','size':15})  # You have to define the font family, text color and text size
plt.title('Sports Watch Data', fontdict={'family':'serif','color':'blue','size':20})

plt.show()

# PART IV - POSITIONING THE TITLE:
# You can position the title by using the 'loc' parameter in the title() function. It can be set to 'left', 'right' or 'center' - the default value is 'center':
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calories Burned")
plt.title('Sports Watch Data', loc='left')  # Position the title on the left side of the graph

# You can plot points, lines, and create labels and titles for your data visualizations! Nice job, and make sure to not lose your momentum! Onto Lesson 4!!
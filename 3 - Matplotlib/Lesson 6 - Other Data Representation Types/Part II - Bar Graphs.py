import numpy as np
import matplotlib.pyplot as plt

# Bar graphs are a data representation type that is best at comparing things to the amount of it that there is (ex: presidential campaigners compared to the amount of votes they get)
# Bar graphs are also useful at showing changes in the number of something over time (ex: highest temperature recorded in Cairo, Egypt between years 2010 to 2020)

# PART II.I.I - DRAWING A CONVENTIONAL BAR GRAPH:
# To draw a bar graph using Matplotlib's Pyplot, you simply use the bar() function and pass the x and y values of the data you want to visualize:

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()
# You will notice that unlike the x-axis values for the scatter graphs, which worked with the y-axis values to make Cartesian coordinates,
# the x-axis values are the headers for each bar, those being 'A', 'B', 'C' and 'D'
# The y-axis values keep the same/similar value, and determine how high the bar goes on the chart

# PART II.I.II - DRAWING A HORIZONTAL BAR GRAPH:
# If you want the bars on your bar graph to go sidewards rather than the standard vertical bars, you can use the barh() function to create a horizontal bar graph:

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)  # The bars of the graph will now appear going sidewards rather than upwards
plt.show()

# PART II.II - CHANGING THE COLOR OF THE BARS:
# The bar() and barh() functions both have a parameter called 'color', which allows you to change the color of the bar to your liking:

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color="red")
plt.show()

plt.barh(x, y, color='magenta')
plt.show()

# You can also use hexadecimal values:

plt.bar(x, y, color='#4CAF50')  # A nice forest green
plt.show()

# PART II.III.I - CHANGING THE WIDTH OF THE BARS:
# The bar() function has a parameter called 'width' which allow you to alter the width of the bars in the graph:
# If 'width' is not defined, then it defaults to 0.8

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width=0.1)  # This will make the bars very thin
plt.show()

# PART II.III.II - CHANGING THE HEIGHT OF THE BARS (HORIZONTAL BAR GRAPHS):
# If you are using a horizontal graph, then you cannot change the width of the bar by using the 'width' parameter.
# Rather, there is a barh() function-specific parameter called 'height'. You use it the same way you would the 'width' parameter:
# If 'height' is not defined, then it defaults to 0.8

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, height=1.5)  # This will make the bars very thick
plt.show()

# PART II.IV - RANDOM PROJECTIONS WITH BAR GRAPHS:
# You can create a random array of values to project a bar graph of random values:

x = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])  # Make an array of 10 columns for the bars to go on
y = np.random.randint(50, size=10)  # Randomly generate 10 integers between 0 and 49

plt.bar(x, y, width=0.5, color='#0fd4c7')  # Draw a bar graph with line width 0.5 and a sky blue color
plt.grid(color='red', linestyle=':', linewidth=0.5)  # Add a grid behind the graph so the user can easily reference how high the values are (remember learning this in past lessons? If not, then look back for it)
plt.title('A Random Set of Values on a Bar Graph!')  # Give the graph a title
plt.show()

# PART II.V - MULTI-BAR BAR CHARTS:
# You can also create a bar chart with multiple bars representing one group (ex: the number of students that passed each sector of engineering college per year)

data = np.array([[30, 25, 50, 20], [40, 23, 51, 17], [35, 22, 45, 19]])
years = np.array([2015, 2016, 2017, 2018])
X = np.arange(4)  # array[0, 1, 2, 3]

fig = plt.figure()  # Create a new figure to put all these values on
ax = fig.add_subplot(1,1,1)  # Because we are working with multiple pieces of data, we need to identify the whole graph as one subplot so that the three bars of each section aren't counted as separate bar graphs
# 1,1,1 = 1x1 array, 1st subplot

# Add in three red, green and blue bars each with all 4 values ('X' makes sure that Matplotlib looks for all 4 instances of an integer)
ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)

ax.set_xticks(X+0.25, years)  # Set the x-axis labels numbers as the 'years' array. X+0.25 centers the label under the center bar of the three bars
ax.set_yticks(np.arange(0,61,5))  # Set the scale on the y-axis going from 0 to 60 while jumping 5 each time (0,5,10,15,20...)
ax.set_title('Amount of Students That Passed Each Sector of the Engineering Course')
ax.set_ylabel('Amount of students that passed')
ax.grid(color='purple', ls='--', lw=0.7, axis='y')
ax.set_axisbelow(True)  # This puts the grid lines below the bars so that they don't overlap
ax.legend(['CS', 'IT', 'E&TC'])
plt.show()

# PART II.VI - STACKED BAR GRAPHS:
# You can also create stacked bar graphs to represent multiple types of data on one bar:

menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
ind = np.arange(5) # array[0,1,2,3,4]

fig = plt.figure()  # Create new figure for subplot
ax = fig.add_subplot(111)  # 1x1 subplot, 1st subplot

ax.bar(ind, menMeans, width=0.35, color='r')  # Make the Men bar red (this will go at the bottom)
ax.bar(ind, womenMeans, width=0.35, bottom=menMeans, color='b')  # Make the Women bar go on top of the Men one (since bottom is menMeans, so womenMeans must be on top) and make it blue

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
ax.set_yticks(np.arange(0, 81, 10))  # Set the scale on the y-axis going from 0 to 80 while jumping 10 each time (0,10,20,30...)
ax.legend(labels=['Men', 'Women'])
plt.show()

# You can add as many bars to the stack as you want. Here's an example of 5 classes' scores per gender:
all_classes_male = np.random.randint(1,21,5)  # Score is between 1 and 20. Does this 5 times
all_classes_female = np.random.randint(1,21,5)  # Score is between 1 and 20. Does this 5 times
ind = np.arange(5)

fig = plt.figure()
ax = fig.add_subplot(111)  # 1x1 array, 1st subplot

ax.bar(ind, all_classes_male, color='blue', width=0.6)
ax.bar(ind, all_classes_female, bottom=all_classes_male, color='hotpink', width=0.6)

ax.set_ylabel('Scores')
ax.set_title('Scores for each class by gender')
ax.set_xticks(ind, ('Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5'))
ax.set_yticks(np.arange(0,21))
ax.legend(labels=['Boys', 'Girls'])
ax.grid(color='k', ls=':', lw=0.5, axis='y')
ax.set_axisbelow(True)

plt.show()

# Now that you have learned how to create bar graphs and manipulate the features of them, you can move onto Part III - Histograms!
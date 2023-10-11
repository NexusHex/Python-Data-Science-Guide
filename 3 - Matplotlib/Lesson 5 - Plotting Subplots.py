import numpy as np
import matplotlib.pyplot as plt

# You don't always want to show just one plot of data, and sometimes you would prefer if you show multiple data plots. Matplotlib allows you to do this pretty easily

# PART I - PLOTTING SUBPLOTS:
# Matplotlib uses a function called subplot() to allow the user to create multiple plots of data at once. It takes three parameters: rows, columns and the plot index:
# The rows and columns determine how large the plot is - inputting 1, 2 for rows and columns will make a 1x2 plot. These values determine how the subplots are arranged (taller plots will be put side by side, while longer plots will be put on top of each other)
# The plot index determines what number plot the plot is - inputting 1 for a plot will make that plot the first plot, while another plot with plot index 2 would be the second plot

# First Plot
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)  # 1x2 plot, first plot
plt.plot(x,y)

# Second Plot
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)  # 1x2 plot, second plot
plt.plot(x,y)

plt.show()  # Both subplots were taller than they were long, so they will be arranged side by side

# If we wanted to arrange these plots on top of each other, we would just have to rearrange the rows and columns so that they are longer than they are tall:

# First Plot
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)  # 2x1 plot, first plot
plt.plot(x,y)

# Second Plot
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)  # 2x1 plot, second plot
plt.plot(x,y)

plt.show()  # Since they are longer than they are tall, they will be arranged on top of each other

# The amount of plots you can draw is limitless, so you just need to define everything and Matplotlib will take care of everything else:

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()

# PART II.I - ADDING TITLES TO YOUR SUBPLOTS:
# You can add titles to each subplot, just like adding a title to a normal plot!

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)
plt.title('Team Red')

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)
plt.title('Team Blue')

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)
plt.title('Team Yellow')

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)
plt.title('Team Green')

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)
plt.title('Team Purple')

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)
plt.title('Team Pink')

plt.show()

# PART II.II - ADDING A MASTER TITLE TO ALL YOUR SUBPLOTS:
# Having a title for each subplot is useful, but we might want to have a big title to sum up everything that the dataset is representing to us
# We can define a master title by using the suptitle() function:

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)
plt.title('Team Red')

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)
plt.title('Team Blue')

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)
plt.title('Team Yellow')

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)
plt.title('Team Green')

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)
plt.title('Team Purple')

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)
plt.title('Team Pink')

plt.suptitle('Team Points Scored Over Time')
plt.show()

# PART III - ADDING SUBPLOTS AND CREATING FIGURES:
# Rather than wasting time creating a new subplot using subplot() every time, we can create something called a figure and add subplots to that figure
# This makes it easier for someone reading the code (as well as shorter for them to read) to understand when a subplot was added to the figure:

y1 = np.array([3, 8, 1, 10])
y2 = np.array([10, 20, 30, 40])

fig = plt.figure()  # We create a new figure to contain all of these new subplots
# We add two subplots to the figure using 'add_subplot()'
# The first two numbers that 'add_subplot()' takes are the dimensions of the subplot. In this example, they are 2 and 2, meaning that it is a 2x2 subplot
# The third number is the number of what subplot it is; 1 = 1st subplot, 2 = 2nd subplot, so on and so forth
ax1 = fig.add_subplot(2,2,1)  # 2x2, 1st subplot
ax2 = fig.add_subplot(2,2,2)  # 2x2, 2nd subplot

ax1.plot(y1)  # Plot the values in 'y1' to the subplot 'ax1' within the figure
ax2.plot(y2)  # Plot the values in 'y2' to the subplot 'ax2' within the figure

plt.show()

# Sometimes, you will make use of subplots just for one plot, since it is easier to make graphs with multiple elements (like a stacked bar graph) in a subplot
# To just have one subplot, you can have the values within 'add_subplot()' set to 1,1,1 (1x1, 1st subplot), since there is no need to define dimensions - it's the only plot there!

# An example of using a subplot just for one plot. You only need to understand the stuff on lines 208 and 209 and realize that the whole thing is just one big plot being put into one subplot:
all_classes_male = np.random.randint(1,21,5)
all_classes_female = np.random.randint(1,21,5)
ind = np.arange(5)

fig = plt.figure()  # !!! Understand this!
ax = fig.add_subplot(111)  # !!! Understand this!

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

# Now that you can create multiple plots and give them all titles, you can start to learn about new data representation media like scatter graphs, pie charts and others! Move onto Lesson 6!
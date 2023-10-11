import numpy as np
from matplotlib.pyplot import show
import seaborn as sns

# The Pareto Distribution is used to show that the level of inputs and outputs is not always equal
# This was discovered by Italian Vilfredo Pareto when he saw that 80% of his country's wealth was in the hands of 20% of its population.
# This became obvious to see in other instances as well, and became a distribution for statistics

# To create a Pareto distribution using Numpy, we can use the np.random.pareto() function, which has two arguments:

# a (Alpha) = Shape parameter (This will determine the slope of the line, higher number = steeper slope + higher start point on y-axis)
# size = Shape of the returned array

# Creating a Pareto distribution with alpha being 2 and the array returned being 2x3:

x = np.random.pareto(a=2, size=(2,3))
print(x)

# Visualizing a Pareto Distribution:

y = np.random.pareto(a=5, size=5000)
sns.distplot(y)  # I will keep both the histogram and the line for this visualization to show how the Pareto distribution shows data
show()

print()
print(y)  # I also want to print this distribution out so that you can see what is going on with the line and histogram

# You will see that the curve and numbers start out really high at first, and quickly go down into low lines. This is Pareto's findings at work, since
# most of the graph's area is in a small part of the line, just like how most of Italy's wealth was in a small population of people.
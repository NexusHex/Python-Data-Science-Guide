import numpy as np
from matplotlib.pyplot import show
import seaborn as sns

# The normal distribution is one of the most important types of distribution on a graph, since it represents a lot of scenarios in statistics.
# It is also called a Gaussian distribution, and is a symmetrical curve that peaks at the center of the graph and has its lowest points at both ends of the graph
# The normal distribution is an indiscreet distribution, meaning that it has an infinite amount of values wiithin it
# We can use the np.random.normal() function to get a normal distribution of values
# It has 3 parameters:
# loc (Mean, Mu) = Where the bell curve peaks
# scale (Alpha, Standard deviation) = How flat the graph distribution will be
# size = The size of the returned array

# We can create a normal distribution with just the 'size' argument filled out:
x = np.random.normal(size=(2,3))  # This will create a 2x3 2D array of random numbers with a normal distribution

# Note that 'loc' is where the curve peaks (the x-axis value where the peak of the curve is)
# And that 'scale' is how flat the curve is (how far off the normal distribution the values can go)
# Using these values, we can control where our distribution peaks and how far off the normal distribution the values can be:

y = np.random.normal(loc=2,  scale=1.5, size=(2,3))  # 2x3 array of normally distributed values, with a curve peak at x=2 and a 1.5 deviation (this means that the whole graph can be moved x=1.5/x=-1.5 to the left or right)

# This is how you can visualize a randomly generated normal distribution:

sns.distplot(np.random.normal(size=1000), hist=False)  # Plot a line following the normal distribution but don't show the histogram that comes with it by default

show()  # Show the graph that we plotted

# If we wanted, we could also show the histogram for extra context:

sns.distplot(np.random.normal(size=1000), hist=True)  # We just need to set 'hist' to True

show()
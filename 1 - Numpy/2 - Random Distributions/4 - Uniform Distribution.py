import numpy as np
from matplotlib.pyplot import show
import seaborn as sns

# Uniform distribution is used to describe the probability of an event happening where all other events have an equal chance of happening (rolling a 1
# on a die)
# It is a discrete distribution, meaning that the amount of events that is has is finite
# You can create a uniform distribution in Numpy using the np.random.uniform() function, which has these three arguments:

# low = Lower bound (smallest number that the uniform distribution can include) - Default is 0.0
# high = Upper bound (largest number that the uniform distribution can include) - Default is 1.0
# size = The size of the returned array

# Here is an example of a uniform distribution array:

x = np.random.uniform(size=(2,3))  # A uniform distribution that is 2x3 in size and has random numbers between 0 and 1
print(x)

# Visualizing a Uniform Distribution:

sns.distplot(np.random.uniform(low=0.5, high=2, size=1000), hist=False)  # Lower bound of 0.5, upper bound of 2 with 1000 values and just the line curve

show()

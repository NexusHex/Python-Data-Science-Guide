import numpy as np
from matplotlib.pyplot import show
import seaborn as sns

# The Chi Square Distribution is used to show whether your data follows another distribution like a Normal or Poisson distribution.
# The distribution uses the Chi Square Test (check https://www.simplilearn.com/tutorials/statistics-tutorial/chi-square-test#:~:text=Chi%2Dsquare%20is%20most%20commonly,of%20this%20type%20of%20research.
# for formula, full explanation and applications) to determine whether a random set of values is equal to an actual set of data.
# An example of using the Chi Square distribution is to compared 100 randomly generated coin tosses to 100 real coin tests to see how closely the random
# results match the real results.

# Note that this distribution is pretty complicated but is also pretty niche, and is usually used to train regression models to better deal with datasets
# Doesn't mean we won't go through it though!

# You can create a Chi Square distribution in Numpy using the np.random.chisquare() function, which has two arguments:
# df = Degree of freedom (this is the number of (rows - 1) * (columns - 1). A 2x2 grid would have a 'df' of 1, because (2-1) * (2-1) = 1)
# size = Shape of the array returned

# Creating a Chi Square Distribution to represent an array with size 2x3 ((2-1) * (3-1) = 1 * 2 = 2) and a 'df' of 2:

x = np.random.chisquare(df=2, size=(2,3))
print(x)

# Visualizing a Chi Square Distribution:

sns.distplot(np.random.chisquare(df=81, size=(10,10)))  # (10-1) * (10-1) = 9 * 9 = 81
show()
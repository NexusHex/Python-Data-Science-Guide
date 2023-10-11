import numpy as np
from matplotlib.pyplot import show
import seaborn as sns

# Logistic Distribution is used to describe growth, and is used mostly in machine learning scenarios where the program is trying and failing to do a
# job it was told to do
# Create a Numpy logistic distribution using np.random.logistic(). Its three functions are:

# loc (Mean, Mu) = Where the peak of the curve is - Default is 0
# scale (Alpha) = Standard deviation of the curve - Default is 1
# size = Size of the returned array

# Here is a 2x3 array logistic distribution with 'loc' at 1 and 'scale' at 2:

x = np.random.logistic(loc=1, scale=2, size=(2, 3))
print(x)

# Visualizing a Logistic Distribution:

sns.distplot(np.random.logistic(size=1000), hist=False)

show()

# Normal vs Logistical Distribution:
# Both distributions are almost the same, but a logistical distribution has more space under the tails of the sides, meaning that there are more possibilities for events to occur in those areas.

sns.distplot(np.random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(np.random.logistic(size=1000), hist=False, label='logistic')

show()
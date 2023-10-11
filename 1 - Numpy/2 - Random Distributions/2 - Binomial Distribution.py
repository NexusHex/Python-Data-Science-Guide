import numpy as np
from matplotlib.pyplot import show
import seaborn as sns

# A binomial distribution is a discrete distribution, meaning that it has a finite amount of values within it
# The distribution is used to determine the result of a binary possibility (2 possibilities), like tossing a coin, since there are only two sides it can land on
# You can create a binomial distribution in Numpy using the np.random.binomial() function. It has 3 arguments:
# n = Number of trials
# p = probability of an occurrence (a coin landing on heads or tails = 0.5 because it's a 50/50 chance)
# size = the shape of the returned array (2x2, 3x4, 50x2 etc.)

# Here is how simulating 10 coin tosses will look like using np.random.binomial():

x = np.random.binomial(n=10, p=0.5, size=1000)  # 10 trials, 50% chance for an outcome, array size of 10 (1 for each trial)
print(x)

# And here is how to visualize a binomial distribution (with 1000 coin tosses this time):

sns.distplot(np.random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
show()

# What's the difference between a normal distribution and a binomial distribution?
# Normal distributions have an infinite amount of events within itself, while a binomial distribution has finite events, but if there are enough results, then the graphs look almost the same:

sns.distplot(np.random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(np.random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()
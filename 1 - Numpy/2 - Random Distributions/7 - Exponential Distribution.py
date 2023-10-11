import numpy as np
from matplotlib.pyplot import show
import seaborn as sns

# Exponential distributions describe the time till the next event happens (how long till the next bus comes, how long it takes for a customer to make
# a purchase etc.)
# To create an exponential distribution in Numpy, you use the np.random.exponential() function, which has these three arguments:

# scale = Inverse of rate (rate is the amount of times that something happens, like how many times a person eats in a day)
# size = Shape of the returned array

# Here is an example of using an exponential distribution with a scale of 2 on a 2x3 array:

x = np.random.exponential(scale=2, size=(2,3))
print(x)

# This would return (random):
# [[0.38111582 5.41502386 2.15079922]
#  [1.62256941 0.21541365 2.38396869]]
# You may be able to tell that the peak of the numbers is already at the second element. An exponential distribution tells us when an event will next
# happen, so what do you think will happen if the size of the array returned is increased?

y = np.random.exponential(scale=2, size=(4,6))
print()
print(y)

# You may see that there is another peak that comes close to the first peak in a larger array of points, meaning that there is a higher chance that the
# event that is being measured will happen. Try running the code a few times and see the assortment of results!

# Visualizing an Exponential Distribution:

sns.distplot(np.random.exponential(scale=5, size=100), hist=False)  # 100 customers take 5 minutes on average to pick up a product
show()

# Poisson vs Exponential Distribution:
# Poisson distribution describes the number of occurrences of an event within a specific time period, while exponential distribution describes the time
# between those specific time periods
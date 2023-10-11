import numpy as np
from matplotlib.pyplot import show
import seaborn as sns

# Poisson distribution is a discrete distribution (finite events) that represents how many times an event can happen in a specified time (if somebody eats twice a day, what is the probability that they will eat thrice?)
# You can create a Poisson distribution in Numpy by using the np.random.poisson() function, which has two arguments:
# lam = rate/number of occurrences (for the example above, it would be two since the person eats twice in a day)
# size = the dimensions of the array returned

# Here's an example of using the Poisson distribution with Numpy to create a random array of 10 values based on the example above says:
x = np.random.poisson(lam=2, size=10)
print(x)

# Visualizing a Poisson distribution:

sns.distplot(np.random.poisson(lam=2, size=1000), kde=False)
show()

# Normal vs Poisson distribution:
# Unlike normal distribution, Poisson distribution has a finite amount of values within itself, but like binomial distribution,
# the curve of the graph eventually reaches the same state as a normal distribution with the right positioning

# Binomial vs Poisson distribution:
# Binomial distributions only have two outcomes, while a Poisson distribution can have as many as it likes. However, once the 'n' argument is very high
# and the 'p' argument is close to 0, (see '2 - Binomial Distribution' for more on these arguments) the curve that the distribution makes becomes almost
# the same as a Poisson curve.

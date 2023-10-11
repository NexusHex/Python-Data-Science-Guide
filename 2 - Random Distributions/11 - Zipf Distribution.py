import numpy as np
from matplotlib.pyplot import show
import seaborn as sns

# A Zipf Distribution is used to show data based on Zipf's Law
# Zipf's Law: In a collection, the nth common term is 1/n times of the most common term (for example, the fifth most popular word is said 1/5 as much as
# the most popular word)

# To create a Zipf distribution using Numpy, you use the np.random.zipf() function, which has two arguments:

# a = Distribution Parameter (the higher 'a' is, the flatter the distribution will be, because the chance for the nth common term to be chosen gets smaller and smaller till they turn out equal)
# size = The size of the array returned

# Drawing a Zipf distribution with a distribution parameter of 2 and an array size of 2x3:

x = np.random.zipf(a=2, size=(2,3))
print(x)

# The higher 'a' is, the smaller the numbers in the distribution will be

print()
y = np.random.zipf(a=3, size=(2,3))
print(y)
print()
z = np.random.zipf(a=4, size=(2,3))
print(z)
# By the time the distribution parameter is 4, almost all the values in the distribution are 1, since the chance for each event to happen gets smaller and smaller every time

# Visualizing a Zipf Distribution:

sns.distplot(np.random.zipf(a=2, size=1000), hist=False)
show()

# Showing just the values under 10 for a more meaningful graph:

a = np.random.zipf(a=2, size=1000)
sns.distplot(a[a<10], kde=False)  # No line, just histogram
show()
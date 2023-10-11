import numpy as np
from matplotlib.pyplot import show
import seaborn as sns


# Rayleigh Distribution is a distribution using the probability density function (Check Matplotlib > Lesson 6 > Part III - Histograms for an explanation for this function)
# It is mainly used in these scenarios:
# Modelling multiple paths of scattered signals reaching a receiver in communications
# Modelling physically scientific things like wave height, wind speed and light radiation
# Measuring the lifetime of things like resistors, transformers and capacitors in engineering
# Measuring noise variance in an MRI scan in medical imaging

# To create a Rayleigh distribution in Numpy, we use the np.random.rayleigh() function which has two arguments:
# scale = Standard deviation (how flat the distribution will be) - Default is 1.0
# size = Shape of the array returned

# Drawing out a Rayleigh Distribution with 'scale' of 2 and 'shape' of 2x3:
x = np.random.rayleigh(scale=2.0, size=(2,3))
print(x)

# Visualizing a Rayleigh Distribution:

sns.distplot(np.random.rayleigh(size=1000), hist=False)
show()

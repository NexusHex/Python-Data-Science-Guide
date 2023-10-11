import numpy as np
import matplotlib.pyplot as plt

# Histograms are graphs used to show frequency distribution (ex: asking 500 people for their shoe size and plotting the distribution of sizes across the graph)
# They are useful when we want to compare multiple different groups to each other, and is very powerful

# PART III.I - CREATING A HISTOGRAM:
# Before we create a histogram, we have to create a pretty large set of values, otherwise the histogram will lack a lot of variety.
# Numpy offers a function called random.normal() to create a distribution of values around a certain number, with a certain limit that it can deviate (be more or less than) the number, as well as the amount of values that are produced

x = np.random.normal(170,10,250)  # Create a normally distributed array concentrated around 170, with a maximum deviation value of 10 (can be maximum 10 more or less than 170) and 250 values
# The assortment of values will be arranged into an array when it is finished being processed, which we can use with Matplotlib
# Now that we have our dataset, we need to create the histogram - we do this by calling the hist() function and passing in our dataset:
plt.hist(x)
plt.show()

# PART III.II.I - PROBABILITY DENSITY FUNCTION:
# Histograms are mostly used to represent a distribution of data across a range of topics like age, gender, shoe size, shirt size etc.
# Histograms are also used with a curved line, called a bell curve, to represent the average number of ever value; it helps to let a person viewing the histogram to predict where a random point may lie on the graph
# Creating this line uses a formula that goes like this:

#                     (-(1 / (2σ²)) . (x - μ)²
#                     -----------------------
#            1                  2σ²
# f(x) = --------- . e
#          √2πσ²

# e = Euler's Number - A mathematical constant approximately equal to 2.71828
# σ = Sigma - The standard deviation of the distribution, which measures how spread out the values are
# π = Pi - A mathematical constant approximately equal to 3.14159
# μ = Mu - The mean (average) of the distribution, which is the center of the curve
# x = All data points on the histogram

# (Don't ask me to explain this, cos I literally have no idea :/ )
# (1 / √(2πσ^2)) - This takes the area UNDER the curve, and makes sure that it is 1

#  (e^((-1 / (2σ²)) * (x - μ)²)) - This defines the shape of the bell curve. Here is a breakdown using the actual names of the numbers:

#       ((-1 / 2(Sigma)²)) * (All data - Mu)²
# Euler

# So in summary, the whole formula in words is:

#                                                                                     ((-1 / 2(Sigma)²)) * (All data points - Mu)²
# The Probability Density Function(for a certain point) = 1 / √2((pi)(Sigma))² x Euler

# Here is an example of using this formula to plot a curved line over a histogram:

bins = 100  # Amount of results we want
mu = 121  # μ value
sigma = 21  # σ value
x = mu + sigma * np.random.randn(1000)  # x value

n, bins, patches = plt.hist(x, bins, density=True, color='green', alpha=0.7)  # Plotting the histogram

y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))  # Using that stupid-ass formula to make the math for our line

plt.plot(bins, y, '--', color='black')  # Plotting the line

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.show()

# PART III.II.II - PLOTTING THE LINE ON THE HISTOGRAM:
# I mean, this was shown for the example in the last part, but whatever:

bins = 100  # Amount of results we want
mu = 121  # μ value
sigma = 21  # σ value
x = mu + sigma * np.random.randn(1000)  # x value

z, bins, patch = plt.hist(x, bins, density=True, color='green', alpha=0.7)  # Plotting the histogram

y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))  # Using that stupid-ass formula to make the math for our line

plt.plot(bins, y, '--', color='black')  # Plotting the line

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.show()

# PART III.III - DIFFERENT COLORED BARS FOR EACH GROUP OF BARS ON THE HISTOGRAM:
# Like how you can make multicolored bar graphs with different colors per category, you can make a multicolored histogram if you want to represent multiple groups of people:
# (We probably need a color break after all that math anyway smh)

n_bins = 20  # Amount of bar groups we want
x = np.random.randn(10000, 3)  # Random int from 0 to 9999, 3 times

colors = ['green', 'blue', 'lime']  # All the colors we want the bars to be

plt.hist(x, n_bins, density=True, histtype='bar', color=colors, label=colors)  # Plot the bar groups with all the customizations we want for it

plt.legend(prop={'size': 10})

plt.show()

# Now that you have learned everything there is to know about histograms, you can move onto learning about pie charts in Part IV!
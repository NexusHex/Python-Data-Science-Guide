from matplotlib.pyplot import show
import seaborn as sns

# In this directory, we will be discussing how to use Numpy to create random distributions with things like graphs and lines
# Matplotlib is a Python library that is proficient in displaying statistical data, but we will only be using a bit of its power for the Numpy tutorial
# Seaborn is another Python library, and this one will be doing all the work of actually plotting the graphs and lines. It's pretty powerful, but I won't be using it outside this tutorial directory
# Here's an example of how Seaborn and Matplotlib can work together to make good-looking graphs (ignore the errors, we won't be needing to update Seaborn any time soon):

sns.distplot([0,1,2,3,4,5], hist=False)

show()

# Good luck with this section of the Numpy directory!
# (all the different distributions will be separated into different files to avoid the reader from getting confused by too much information)
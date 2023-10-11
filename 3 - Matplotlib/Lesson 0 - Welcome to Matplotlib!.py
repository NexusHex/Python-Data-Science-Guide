# Welcome! Matplotlib is a Python library used as a data visualization tool, allowing the coder to show datasets in graphical form in common media like pie charts, bar charts, line graphs and scatter graphs
# To start, we can import the Matplotlib library, but rather than just leaving it there, we need to import a submodule of the library, called pyplot!
import matplotlib.pyplot as plt  # I am using the short name of plt for ease of calling the library
# Most of Matplotlib's utilities lie under this pyplot submodule

# Now that we have Matplotlib imported, we need something to create the data for pyplot to visualize! I will use another popular data science library for Python, Numpy:
import numpy as np
# If you don't know much about Numpy, then navigate to the 'Numpy' folder in this Project's directory

# Here is a quick example of what you can do with Matplotlib's visualization powers! Try running this file...
# Drawing a line in a diagram from coordinates (0,0) to (6,250):
x_points = np.array([0, 6])
y_points = np.array([0, 250])

plt.plot(x_points, y_points)
plt.show()

# Go off to the other files in this folder to learn more about this amazing module! Bye!
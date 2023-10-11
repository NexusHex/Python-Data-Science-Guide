import pandas as pd
import matplotlib.pyplot as plt  # We will be using matplotlib in this file, since Pandas does not have the ability to plot data, but can interface with matplotlib to plot the data :)
# Note that pyplot is a submodule of the matplotlib module

# When you have a finished dataset, and would like to project it into a discernible form, like a line graph or bar chart, then Pandas allows you to connect to another module, Matplotlib, and plot your data as a graph!
data_frame = pd.read_csv('data.csv')
# We can use the Pandas method .plot() to create a base so we can plot the data:
data_frame.plot()
# And now we can use our other module, Matplotlib, to project this plotted data into a graph! (Don't worry about knowing or not knowing matplotlib commands for this set of guides, you can learn more about the module in the 'Matplotlib' folder)
plt.show()

# Use plotting to show your data to others, so they can understand what's going on with your data!
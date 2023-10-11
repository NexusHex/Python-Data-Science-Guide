import numpy as np
import matplotlib.pyplot as plt

# For the past 5 lessons, we have worked with line graphs, which are the default data representation that Matplotlib uses to show the data you put
# into the library, but you can opt for using other data representation types like scatter graphs or histograms

# PART I - SCATTER GRAPHS:
# Scatter graphs are a data representation type that allows you to show an assortment of data points across a chart in comparison to (usually) two values
# We can use Matplotlib's scatter() function to create a scatter graph, but we first need to create equally-sized arrays so the scatter graph actually has information to do!

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# Now that we have two equally-sized arrays, we can tell Matplotlib to plot those points on a scatter graph:
plt.scatter(x, y)
plt.show()

# This scatter graph represents the age of a car compared to how fast it drives, so let's give it some labels to make it easier to read, like we learned in Lesson 3:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.xlabel('Car Age')
plt.ylabel('Car Speed')
# We could also add grid lines to make it easier to see where the points are on the graph
plt.grid(color='green', linestyle='--', linewidth=0.5)
plt.show()
# Now our graph is easier to understand

# PART I.I - COMPARING SCATTER GRAPHS:
# Say we went back to the same road we went to see the cars' ages and speed like the graph above this part and took another day's worth of data.
# Wouldn't it be useful to compare the two days' data together and see the differences/similarities? Matplotlib lets us do this pretty easily:

# Day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
plt.xlabel('Car Age')
plt.ylabel('Car Speed')
plt.grid(color='green', linestyle='--', linewidth=0.5)

# Day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)
plt.xlabel('Car Age')
plt.ylabel('Car Speed')
plt.grid(color='green', linestyle='--', linewidth=0.5)

plt.show()

# You may notice that Matplotlib automatically changes the color of the 2nd set of points, so you don't get confused - we will learn how to change these colours later on

# PART I.II.I - SETTING COLORS FOR SCATTER GRAPH POINTS:
# You can set your own colors for the points manually by changing the 'color' parameter using any of the accepted colors:

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color='hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color='#88c999')

plt.show()

# PART I.II.II - SETTING COLORS FOR INDIVIDUAL POINTS:
# If you want every point in the scatter graph to have a different color, then you can do so by setting the 'color' parameter to an array of colors that you want each point to be. Make sure that there are as many colors as there are points:

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, color=colors)

plt.show()  # Now all the points are different colors

# PART I.III - COLOR MAPS:
# In statistics, people use another data visualization method to show the relevance of a comparison, called a colormap.
# A colormap is like a list of colors ranging from 0 to 100, where 0 is one color and 100 is the opposite color on the color spectrum (ex: purple=0, yellow=100)
# You can use colormaps to show the relevance of a point in a scatter graph based on how high they rank on the color map, since their color will change depending on its position on the map:

# A colormap going from purple to yellow is an in-built colormap in Matplotlib called 'Viridis', so we need to use that name to call the colormap we want
# We also need to give the colormap a scale, so it knows how big it should be. We will pass an array from 0 to 100 going up in 10s, so it has an equal scale going from 0 to 100

# We can pass in all of this information through the 'c' and 'cmap' parameters.
# 'c' will take the array from 0 to 100, since the colormap will use it to determine where the colors are on the colormap based on the numbers
# 'cmap' will take the name of the colormap we want to use. We will be using 'Viridis', as mentioned before:

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])  # x-axis point positions
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])  # y-axis point positions
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])  # Scale that we will be using for the colormap to determine what color the points are

plt.scatter(x, y, c=colors, cmap='viridis')  # Create a scatter graph with the c value of the array going from 0 to 100, and the colormap type being set to 'Viridis'
plt.grid(color='red', linestyle='--', linewidth=0.5)  # Adding grid lines to make everything easier to see

plt.show()

# If you want to include the colormap beside the scatter graph (which you would most of the time), then simply add the colorbar() function before you show() the graph

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')
plt.grid(color='red', linestyle='--', linewidth=0.5)
plt.colorbar()  # Adding the colormap beside the graph

plt.show()

# PART I.IV - VALID COLORMAP NAMES:
# These are all the available colormaps in Matplotlib (it's a lot ikr)
# NOTE: Copied from w3school's Matplotlib tutorial (https://www.w3schools.com/python/matplotlib_scatter.asp)

# Name           Reversed Colors

# Accent		    Accent_r
# Blues		 	    Blues_r
# BrBG		 	    BrBG_r
# BuGn		 	    BuGn_r
# BuPu		 	    BuPu_r
# CMRmap	 	    CMRmap_r
# Dark2		 	    Dark2_r
# GnBu		 	    GnBu_r
# Greens	 	    Greens_r
# Greys		 	    Greys_r
# OrRd		 	    OrRd_r
# Oranges	 	    Oranges_r
# PRGn		 	    PRGn_r
# Paired   	        Paired_r
# Pastel1		    Pastel1_r
# Pastel2	 	    Pastel2_r
# PiYG		 	    PiYG_r
# PuBu		 	    PuBu_r
# PuBuGn	 	    PuBuGn_r
# PuOr		 	    PuOr_r
# PuRd		 	    PuRd_r
# Purples	 	    Purples_r
# RdBu		 	    RdBu_r
# RdGy		 	    RdGy_r
# RdPu		 	    RdPu_r
# RdYlBu	 	    RdYlBu_r
# RdYlGn	 	    RdYlGn_r
# Reds		 	    Reds_r
# Set1		 	    Set1_r
# Set2		 	    Set2_r
# Set3		 	    Set3_r
# Spectral	 	    Spectral_r
# Wistia	 	    Wistia_r
# YlGn		 	    YlGn_r
# YlGnBu	 	    YlGnBu_r
# YlOrBr	 	    YlOrBr_r
# YlOrRd	 	    YlOrRd_r
# afmhot	 	    afmhot_r
# autumn	 	    autumn_r
# binary	 	    binary_r
# bone		 	    bone_r
# brg		 	    brg_r
# bwr		 	    bwr_r
# cividis	 	    cividis_r
# cool		 	    cool_r
# coolwarm	 	    coolwarm_r
# copper	 	    copper_r
# cubehelix	 	    cubehelix_r
# flag		 	    flag_r
# gist_earth 	    gist_earth_r
# gist_gray	 	    gist_gray_r
# gist_heat	 	    gist_heat_r
# gist_ncar	 	    gist_ncar_r
# gist_rainbow 	    gist_rainbow_r
# gist_stern	    gist_stern_r
# gist_yarg	 	    gist_yarg_r
# gnuplot		    gnuplot_r
# gnuplot2	 	    gnuplot2_r
# gray		 	    gray_r
# hot		 	    hot_r
# hsv		 	    hsv_r
# inferno	 	    inferno_r
# jet		 	    jet_r
# magma		 	    magma_r
# nipy_spectral	    nipy_spectral_r
# ocean		 	    ocean_r
# pink		 	    pink_r
# plasma	 	    plasma_r
# prism		 	    prism_r
# rainbow	 	    rainbow_r
# seismic	 	    seismic_r
# spring	 	    spring_r
# summer	 	    summer_r
# tab10		 	    tab10_r
# tab20		 	    tab20_r
# tab20b	 	    tab20b_r
# tab20c	 	    tab20c_r
# terrain	 	    terrain_r
# twilight	 	    twilight_r
# twilight_shifted	twilight_shifted_r
# viridis		 	viridis_r
# winter		 	winter_r

# PART I.V - GRAPH POINT SIZES:
# You can change the sizes of the points in the graph by passing an array of values (same length as other all values' arrays) into the 's' parameter in the scatter() function:

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes)  # Passing in the array of point sizes that we want the points to have

plt.show()

# PART I.VI - GRAPH POINT TRANSPARENCY:
# You can also change the transparency of the points on the scatter graph by passing a float into the 'alpha' parameter:

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)  # Telling Matplotlib that we need every point to have a transparency of 0.5 (50%)

plt.show()

# PART I.VII - COMBINING POINT SIZES, TRANSPARENCY AND COLORMAPS:
# Using the last three things we learned, we can create a random group of points, positions, colors, sizes, transparency and color and put it into one scatter graph to make it look like a realistic piece of data:

x = np.random.randint(100, size=100)  # Create a randomly generated array of values between 0 and 99 with 100 values for the x coordinates
y = np.random.randint(100, size=100)  # Create a randomly generated array of values between 0 and 99 with 100 values for the y coordinates
colors = np.random.randint(100, size=100)  # Create a randomly generated array of values between 0 and 99 with 100 values for the position of the data point on the colormap, determining its color
sizes = 10 * np.random.randint(100, size=100)  # Create a randomly generated array of values between 0 and 99 with 100 values for the size of every point

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')  # We will use a different colormap style this time

plt.colorbar()

plt.show()

plt.show()

# That ends this part of Lesson 6! The next part will cover bar charts, so make sure to go there once you're done!
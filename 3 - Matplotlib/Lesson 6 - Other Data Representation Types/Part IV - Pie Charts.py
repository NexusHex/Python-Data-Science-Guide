import numpy as np
import matplotlib.pyplot as plt

# Pie charts represent data as parts of a whole. They are useful for comparing different amounts of things available across different circumstances
# (ex: tonnes of aluminium per continent)

# PART IV.I - CREATING A PIE CHART:
# To create a pie chart, you use the pie() function and pass in the percentages of the chart that each segment takes up:

segments = np.array([35, 25, 25, 15])  # 4 segments that all add up to 100% (make sure that they add up to 100!!!!)
plt.pie(segments)
plt.show()
# The size of each segment is calculated using this formula: x/sum(x)
# This means: the value divided by the sum of all values
# For example, one of the sizes of our segments would be this:
# 35 / (35 + 25 + 25 + 15) -> 35 / 100 = 35%
# Therefore, the amount of the chart that this segment takes up is 35%

# PART IV.II - SEGMENT LABEL:
# Like any conventional pie chart, you can add labels for each segment, so you can easily see the difference and comparisons between them
# To add names for segment labels, you pass values into the 'labels' parameter in the form of a list:

y = np.array([35, 25, 25, 15])
my_labels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=my_labels)
plt.show()

# PART IV.III - START ANGLE:
# By default, Matplotlib starts the segments from the beginning of the array that was passed in and starts at the x-axis
# A diagram to explain:
#                          90° | y+ <_______
#                              |            \
#                    x-        |         x+  |
#                    ----------|----------  <---- Matplotlib starts from here by default and goes anticlockwise from there
#                   180°       |         0°
#                              |
#                         270° | y-

# If you don't want this to be the default start-point, then you can pass your desired start-point into the 'startangle' parameter in the pie() function:

y = np.array([35, 25, 25, 15])
my_labels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=my_labels, startangle=90)  # We set the starting point for segments to 90° (y-axis)
plt.show()

# PART IV.IV - EXPLODE A SEGMENT(S):
# If you want a segment to stand out, then you can change the 'explode' parameter in the pie() function.
# It requires you to supply a list of values for all the values in the bar graph representing how far from the graph's center it is:

y = np.array([35, 25, 25, 15])
my_labels = ["Apples", "Bananas", "Cherries", "Dates"]
explode_vals = [0.2, 0, 0, 0]

plt.pie(y, labels=my_labels, explode=explode_vals)  # Pass the 'explode_vals' list into the 'explode' parameter to explode a certain segment of the chart
plt.show()

# PART IV.V - ADDING SHADOWS TO YOUR CHART:
# If you want to add a bit of texture to your pie chart, then you can alter the 'shadow' parameter in the pie() function to make the chart seem like it has a shadow:

y = np.array([35, 25, 25, 15])
my_labels = ["Apples", "Bananas", "Cherries", "Dates"]
explode_vals = [0.2, 0, 0, 0]

plt.pie(y, labels=my_labels, explode=explode_vals, shadow=True)  # By default, 'shadow' is set to False
plt.show()

# PART IV.VI - CHANGING THE COLORS OF THE SEGMENTS:
# If you want to customize the colors of your pie chart to your liking, then you can do so by telling the 'colors' parameter within the pie() function all the colors you want.
# Note that they have to be passed into the parameter as a list, like the 'explode' parameter does, so you need to explicitly tell Matplotlib what colors you want for each segment:

y = np.array([35, 25, 25, 15])
my_labels = ["Apples", "Bananas", "Cherries", "Dates"]
my_colors = ["black", "hotpink", "b", "#4CAF50"]  # Creating a list of colors that we want our segments to have

plt.pie(y, labels=my_labels, colors=my_colors, shadow=True)
plt.show()
# Note that you can use worded names for colors, as well as short names and hexadecimal codes for customizing your colors

# PART IV.VII.I - ADDING A LEGEND TO YOUR PIE CHART:
# To add a legend of all the names of the segments, you simply use the legend() function before you show() the pie chart:

y = np.array([35, 25, 25, 15])
my_labels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=my_labels)
plt.legend()
plt.show()

# PART IV.VII.II - ADDING A TITLE TO OUR LEGEND:
# To add a title to the legend, we pass a string into the 'title' parameter within the legend() function to give it a title:

y = np.array([35, 25, 25, 15])
my_labels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=my_labels)
plt.legend(title='Class 1\'s favorite fruits')
plt.show()

# PART IV.VIII - LABELS WITHIN SEGMENTS:
# You can add labels to your pie chart to label each segment, but if you want to put another value or name within the segment itself, then you can use the 'autopct' parameter within the pie() function to add a name:

y = np.array([35, 25, 25, 15])
my_labels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=my_labels, autopct='%1.1f%%')  # You don't really need to know what this is, just that this means you will see the percentage of the chart that the segment takes u
plt.show()
# Now you can see the percentages of the chart that the segments take up in the centers of each segment

# PART IV.IX - ADDING A FRAME TO YOUR PIE CHART:
# To add a frame to a Matplotlib pie chart, you set the 'frame' argument to True in the pie() function:

y = np.array([35, 25, 25, 15])
my_labels = ["Apples", "Bananas", "Cherries", "Dates"]
explode_vals = np.array([0.2, 0.1, 0.1, 0.05])

plt.pie(y, labels=my_labels, explode=explode_vals, shadow=True, frame=True)
plt.show()
# Of course, we don't exactly need a numbered frame, but it may be useful if we want to present this pie chart along with something like a line graph in the background

# PART IV.X - BAR GRAPH OF A PIE SEGMENT:
# This part is probably the most complicated, so hang tight! I'll try my best to explain everything that's going in the comments...
# Sometimes, we want to look even further into a segment and see how many people from each segment had a certain aspect
# (ex: a pie graph of voters that agreed, disagreed and didn't decide. We make a bar graph to see the age groups of the people who agreed):

# Make figure and assign axis objects
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))  # Since we are using two plots instead of just one, we need to make use of subplots. 'ax1' will be used for the pie chart, and 'ax2' will be used for the bar graph
fig.subplots_adjust(wspace=0)  # Space so that the two graphs aren't close together

# Pie chart parameters
overall_ratios = [.27, .56, .17]  # These are the rations of the voters that were recorded (agree, disagree, undecided)
labels = ['Approve', 'Disapprove', 'Undecided']  # Labels for the pie chart
explode = [0.1, 0, 0]  # Exploding the first value (agree) so we can tell that the bar graph refers to this result

# Rotate so that first wedge is split by the x-axis
angle = -180 * overall_ratios[0]
wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle, labels=labels, explode=explode)  # This is just so the 'agree' segment is facing the bar graph (makes it easier to reference the segment to the graph)

# Bar chart parameters
age_ratios = [.33, .54, .07, .06]  # These are the number of people in age groups of the people who agreed
age_labels = ['Under 35', '35-49', '50-65', 'Over 65']  # Labels for the age groups
bottom = 1  # Coordinates for the bottom of the bar chart
width = .2  # Width of bar chart

# Adding from the top matches the legend.
for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):  # For every value of the values in 'age_ratios' and 'age_labels' (the lists are reversed)
    bottom -= height  # height would be whatever the 'age_ratios' value is, so 1-0.33, 1-0.54, 1-0.07 and 1-0.06 to get the final height of the bar graph at the end
    bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label, alpha=0.1 + 0.25 * j)
    # Create a bar graph with height=bottom-height and width=0.2. Also set the color to the default: C0 (blue), set the label to the current index of 'label' in this iteration of the for look, and make the transparency 0.1 + 0.25 * the iteration number that the for loop is in (1, 2, 3, 4)
    ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')  # Label the bar graph with the percentage of the bar graph that it takes

ax2.set_title('Age of people who approved')
ax2.legend()
ax2.axis('off')  # Hide all axis decorations from the bar graph so that the bar graph has no scale going along it
ax2.set_xlim(- 2.5 * width, 2.5 * width)  # Setting padding/borders for the bar graph

plt.show()

# You could also draw lines linking the segment and the bar chart, but that would take a lot of math skills and we're not here to do that :p

# Well done on learning everything about pie charts! This marks the end of the Matplotlib walkthrough, so make sure you know everything about the topic and go off to do something cool with this powerful library! Bye!!

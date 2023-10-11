import pandas as pd

# This is the dataset we will use for this file. Check it out in the project folder if you wish to look at it closely:
data_frame = pd.read_csv('data_correlations_dataset.csv')

# Correlations in data are things that are similar to each other, like an upwards trend or a group of outliers. A powerful aspect of Pandas is its ability to see the correlations between points of data in a dataset, and project them concisely to the user.
# Pandas packs most of its correlation-finding power into one command: .corr(). You simply mention the method after an already defined data frame and return it:
print(data_frame.corr())

# Figure I - Data Frame Correlation:
#           Duration     Pulse  Maxpulse  Calories
# Duration  1.000000 -0.155408  0.009403  0.922717
# Pulse    -0.155408  1.000000  0.786535  0.025121
# Maxpulse  0.009403  0.786535  1.000000  0.203813
# Calories  0.922717  0.025121  0.203813  1.000000

# Explanation -
# When finding the correlations in a data frame, Pandas looks through the columns of the data frame
# Pandas shows the correlations between elements in a data frame by numbering them between -1 and 1. There is no name for this, but I will call it a correlation value
# If the correlation value is 1, that means the relationship between the two columns are a 1 : 1 ratio (when one value goes up, the other goes up at exactly the same rate). An example of a correlation value 1 comparison is below:

# Figure II - Correlation Value 1:
# Column A    |    Column B
# 1 (+1)      |    1 (+1)
# 2 (+1)      |    2 (+1)
# 3 (+1)      |    3 (+1)

# If the correlation value is -1, that means the relationship between the two columns are a 1 : -1 or -1 : 1 ratio, meaning that when one value goes up/down, the other goes down/up at the same rate (for example, if column A adds 1 every new row, column B would subtract 1 every new row, looking something like the figure down below)

# Figure III - Correlation Value -1:
# Column A    |    Column B
# 1 (+1)      |    -1 (-1)
# 2 (+1)      |    -2 (-1)
# 3 (+1)      |    -3 (-1)

# The correlation values that Pandas gives you can help you to determine whether the values in your dataset are well correlated, since a good correlation means that other results can be predicted with ease, as well as other reasons
# A good correlation value to have is anything above 0.6 or below -0.6, since its well above half as likely that two values will both go up or that one will definitely go down
# Something like a correlation value of 0.2 is bad, since that is around a 20% chance of both values to go up, which isn't a good chance at all
# -0.3 is also a good example of a bad correlation value (30% chance for one value to go down and the other to go up, not very good chances)

# If you refer to Figure I, you will see a multitude of correlation values:
# Perfect Correlation -
# This is when the correlation value is 1, like you can see in the 'Duration' and 'Duration' cell of the returned table. This makes sense, since a column would be the same as itself

# Good Correlation -
# This is when the correlation value is high/low enough that we can reliably guess what a potentially new value could be. The 'Duration' and 'Calories' cell of the table got a 0.922721 correlation value, meaning that we can pretty accurately say that when the duration increases, so do the calories burnt

# Bad Correlation -
# This is when the correlation value is too low/high to reliably predict the value of a new element. The 'Duration' and 'Maxpulse' correlation value was 0.009403, meaning that we cannot accurately say that the maximum pulse goes higher or lower depending on the duration


# In conclusion, you can use the correlation between values in a data frame to determine the predictability of a new value as well as the patterns between elements. It is very useful for creating data that needs to persuade a certain point, like proving that more ice melting is directly correlated to the Earth's temperature going up.

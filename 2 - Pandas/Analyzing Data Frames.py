import pandas as pd

# The most common way to analyze a data frame is to use the head() method, which shows the data frame from the top with the amount of rows specified:
data_store = pd.read_csv('data.csv')
print(data_store.head(10))  # Reads the first 10 rows of the data frame

# This would return:
#   Duration  Pulse  Maxpulse  Calories
# 0        60    110       130     409.1
# 1        60    117       145     479.0
# 2        60    103       135     340.0
# 3        45    109       175     282.4
# 4        45    117       148     406.0
# 5        60    102       127     300.0
# 6        60    110       136     374.0
# 7        45    104       134     253.3
# 8        30    109       133     195.1
# 9        60     98       124     269.0
# Note: if a parameter for the amount of rows shown isn't specified, then Pandas will return the first 5 rows of the data frame
print(data_store.head())  # We didn't specify the rows parameter, so Pandas will return the first 5 by default

# This would return:
#    Duration  Pulse  Maxpulse  Calories
# 0        60    110       130     409.1
# 1        60    117       145     479.0
# 2        60    103       135     340.0
# 3        45    109       175     282.4
# 4        45    117       148     406.0

# There is also a tail() method for seeing rows from the bottom up:
# Note that the same rules for a lack of a row parameter will also show the last 5 rows
print(data_store.tail())  # Prints the last 5 rows of the data frame

# This would return:
#      Duration  Pulse  Maxpulse  Calories
# 164        60    105       140     290.8
# 165        60    110       145     300.0
# 166        60    115       145     310.2
# 167        75    120       150     320.4
# 168        75    125       150     330.4

# Pandas has a useful method called info() that lets you see the information to do with the data frame that you mention
print(data_store.info())

# This would return:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 169 entries, 0 to 168
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  169 non-null    int64
#  1   Pulse     169 non-null    int64
#  2   Maxpulse  169 non-null    int64
#  3   Calories  164 non-null    float64
# dtypes: float64(1), int64(3)
# memory usage: 5.4 KB
# None
# EXPLANATION:
# There are 169 entries (rows) and 4 columns
# The info() method provides the names of each column along with their index (Duration, Pulse, Maxpulse etc.)
# The information shown also shows how many non-null values are in each column; a null value is a value that is empty or wasn't defined. They are useful for cleaning up the data when you use Pandas to remove and add certain values you want/don't want
# You can see that there are 164 non-null values in the Calories column, rather than the 169 that every other column has. That means there are 169 - 164 = 5 null values in the Calories column
# Note how the Dtype of the Calories column is float64 instead of int64
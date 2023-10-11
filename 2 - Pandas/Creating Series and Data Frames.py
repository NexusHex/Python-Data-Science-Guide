import pandas as pd

# A Series is a one-dimensional array of data in a list:
series = pd.Series([1,2,3,4,5,6,7,8,9,10])  # Notice how the values have been put into a list
print(series)

# This would return:
# 0  1
# 1  2
# 2  3
# 3  4
# 4  5
# 5  6
# 6  7
# 7  8
# 8  9
# 9  10
# dtype: int64
# The first number is the index of the element (item in the series), and the second number is the element itself

# To access a value within a Pandas Series, you can use the index of the element:
index_from_series = series[3]  # This would be index 3 of the series: 4
print(index_from_series)

# This would return:
# 4

# If you don't want to have the default index values as the indexes for the elements, you can define them yourself using the 'index' parameter:
series_contents = [1, 2, 3, 4, 5]
series_with_custom_indexes = pd.Series(series_contents, index=['First', 'Second', 'Third', 'Fourth', 'Fifth'])
print(series_with_custom_indexes)

# This would return:
# First   1
# Second  2
# Third   3
# Fourth  4
# Fifth   5
# dtype: int64

# Now that the series has custom indexes, we can fetch values from that series using those new indexes:
print(series_with_custom_indexes['Fourth'])  # Fetches the element with index 'Fourth', which is 4, and prints it

# This would return:
# 4

# If you want to only take certain values from a set of data then you can define the whole set in a dictionary and fetch certain values from it using the index parameter
dictionary = {'num1' : 1, 'num2' : 2, 'num3' : 3, 'num4' : 4, 'num5' : 5}
series = pd.Series(dictionary, index=['num2', 'num4'])  # Only takes the elements from the dictionary with the indexes 'num2' and 'num4'
print(series)

# This would return:
# num2  2
# num4  4
# dtype: int64
# Note how none of the other values were fetched. Also note how you would have to use the custom indexes ('num2', 'num4') to fetch those values

# ----------------------------------------------------------------------------------------------------------------------

# Data Frames are another Pandas datatype. Like how a Series is like a list, Data Frames are like a table. They are two-dimensional.
data = {  # Creating a dictionary to hold all the values we need to put into the Data Frame
    'day' : ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'],
    'attendance' : [28, 27, 30, 25, 29]
}
data_frame = pd.DataFrame(data)  # Putting the values from that dictionary into a Pandas Data Frame
print(data_frame)

# This would return:
#      day  attendance
# 0  Day 1          28
# 1  Day 2          27
# 2  Day 3          30
# 3  Day 4          25
# 4  Day 5          29
# dtype: int64
# A Pandas Data Frame is basically a table with columns and rows

# If you want to find a certain row within a Data Frame, then you can use the loc attribute to find it:
print(data_frame.loc[0])  # Fetches the row with index 0 (the first row)

# This would return:
# day           Day 1
# attendance       28
# Name: 0, dtype: object
# When you fetch a single row from a Pandas Data Frame, it returns a Series
# Note how the 'Name' attribute of the Series is 0, since the index that got fetched was 0

# Use the loc attribute to return multiple rows:
print(data_frame.loc[[0,1,2]])  # Fetch the first 3 rows of the Data Frame (note how the indexes are put into a separate list when multiple ones are mentioned

# This would return:
#     day  attendance
# 0	Day 1          28
# 1	Day 2	       27
# 2	Day 3	       30
# When you use a nested list to return multiple indexes, the returned value is a Pandas Data Frame

# Naming the indexes in a Data Frame:
data = {
    'student' : ['Jake', 'Kate', 'Nathan', 'Gary', 'Matt'],
    'attendance' : [28, 27, 30, 25, 29]
}
data_frame = pd.DataFrame(data, index=['Person1', 'Person2', 'Person3', 'Person4', 'Person5'])
print(data_frame)

# This would return:
#         student  attendance
# Person1    Jake          28
# Person2    Kate          27
# Person3  Nathan          30
# Person4    Gary          25
# Person5    Matt          29
# To locate a row from this data frame, you use the custom index that was given to the row (Person1, Person2, Person3 etc.)

# If you have data in a separate file, like a CSV or JSON file, you can access those with Pandas as well:
# Accessing a CSV file with Pandas:
# (make sure that the CSV file is in the same directory as the Python file, otherwise you will have to type out the whole PATH of the file)
data_frame = pd.read_csv('data.csv')
print(data_frame)

# The returned value from this code is bigger than the standard for Pandas, so it would return the first and last 5 rows.
# To get a whole data frame, you can use the .to_string() attribute:
print(data_frame.to_string())

# To change the limit where Pandas shows only the first and last 5 rows, you can alter the pd.options.display.max_rows statement:
pd.options.display.max_rows = 200
# The default value is 60. You can change this however you like
# Now we can print out the whole data frame without using the .to_string() attribute:
print(data_frame)
pd.options.display.max_rows = 60  # Resetting the max_rows value for the next topic...

# You can also access JSON files using Pandas:
data_frame = pd.read_json('datafile.json')
print(data_frame)
# Like the CSV file, this JSON file will be too big for the program to print out at once, so we have to change the max_rows value or use the .to_string() attribute:
print(data_frame.to_string())
pd.options.display.max_rows = 9999
print(data_frame)

# JSON files are made with the same format as a Python dictionary, so if you want to put the data into the data frame within your code then you can use a dictionary:
dictionary = {
    'Duration' : {
        "0":60,
        "1":60,
        "2":60
    },
    'Pulse' : {
        "0":110,
        "1":117,
        "2":103
    },
    'Max Pulse' : {
        "0":130,
        "1":145,
        "2":135
    },
    'Calories' : {
        "0":409,
        "1":479,
        "2":340
    }
}

data_frame = pd.DataFrame(dictionary)
print(data_frame)
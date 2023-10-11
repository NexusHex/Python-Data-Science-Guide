import pandas as pd

# Data cleaning is getting rid of bad data in your dataset. Bad data can be:
# - Empty cells
# - Data in the wrong format
# - Incorrect data
# - Duplicate data

# We will me using this data set to practice data cleaning:
data_frame = pd.read_csv('data_cleaning_dataset.csv')
# Check the directory of this file if you want to look at the file itself
# There is another duplicate CSV file called 'data_cleaning_dataset_original.csv' which will remain unchanged by the code, so look at that whenever you need to see the state of the data frame before we make any changes with it

# CLEANING EMPTY CELLS:
# Having empty cells may cause a program to throw an error due to the lack of a piece of information

# Removing Rows with Empty Cells -
# One way to clean the empty cells in a data frame is to remove the whole row of values from the file. This usually won't affect the performance of the data frame since most of them are big enough that >10 changes won't really make a difference
# You can use the .dropna() method to create a new data frame minus any rows that have empty cells:
df_without_empty = data_frame.dropna()
print(df_without_empty)
# This doesn't affect the original data frame

# If you want to directly change the data frame, you can change the 'inplace=False' argument to True:
data_frame.dropna(inplace=True)
print(data_frame)  # This would return the same data frame without any empty cells AND without having to make a new variable to store a copy

# Replacing All Empty Cells -
# Another way to clean up empty cells in your data is to add/replace values into those cells, so that they aren't empty anymore
# This can be done with the .fillna() method (note that we still have to define the 'inplace=False' argument to True for it to work)
data_frame.fillna(130, inplace=True)  # This will replace all empty cells with cells containing the integer 130
print(data_frame)
# None of the rows of the data were lost, and the cells are no longer empty

# Replacing a Certain Column of Empty Cells -
# If you don't want to give the same value to all empty values across all columns, then you can define the column you are changing along with the .fillna() method:
data_frame['Calories'].fillna(130, inplace=True)  # Only replaces all empty cells in the 'Calories' row with the integer 130
print(data_frame)

# Replace a Certain Column of Empty Cells using the Mean, Median or Mode -
# Mean -
# Calculate the mean (average) of all the values in a certain column and replace all empty cells with that mean value:
mean = data_frame['Maxpulse'].mean()
data_frame['Maxpulse'].fillna(mean, inplace=True)  # Replaces all empty cells in the 'Maxpulse' column with the mean of all the values in the column
print(data_frame)

# Median -
# Calculate the median (midpoint) of all the values in a certain column and replace all empty cells with that median value:
median = data_frame['Duration'].median()
data_frame['Duration'].fillna(median, inplace=True)  # Replaces all empty cells in the 'Duration' column with the median of all the values in the column
print(data_frame)

# Mode -
# Calculate the mode (most frequently appearing number) of all the values in a certain column and replace all empty cells with that modal value:
mode = data_frame['Calories'].mode()
data_frame['Calories'].fillna(mode, inplace=True)  # Replaces all empty cells in the 'Calories' column with the mode of all the values in the column
print(data_frame)

# Replacing Certain Empty Cells Using Indexes:
# Like how we can directly change the value of an element using its index if the dataset was defined within the main file, we can access the index of a value even when it is outside a file using the .loc() method
# For example, there is nothing in cell 20 of the Calories column, so we can use the index of that value to find and change it:
data_frame.loc[20, 'Calories'] = 244

# CLEANING DATA OF THE WRONG FORMAT:
# Data in the wrong format is any data that is different to the other datatypes in the data frame (a float in a column of integers, or a null value in a column of strings)

# Converting Cells into the Correct Format -
# If you check the file 'data_cleaning_dataset_original.csv', you'll see that cells 24 and 28 in column 'Date' are not in the same format as the rest of the dates - the dates are strings, while cell 24 is a null value (nothing's there) and cell 28 is an integer
# Pandas has a useful method called pd.to_datetime(), which changes the value(s) put into the method into a date/time value:
data_frame['Date'] = pd.to_datetime(data_frame['Date'], format='mixed')
print(data_frame)
# All the dates will now be properly formatted for usage

# Removing Rows with the Incorrect Format -
# If removing a whole row from a data frame won't affect the performance of the program overall, then you can use the .dropna() method to take out any rows with a null value (You have to define the column(s) that you are looking for null values in by defining the 'subset' argument):
data_frame.dropna(subset=['Date'], inplace=True)  # Drops all rows with null values that are found in the 'Date' column

# INCORRECT DATA:
# Incorrect data does not have to be of the wrong format or an unfilled cell; rather, it can just be a value that someone typed in wrong, like saying something costs $19.90 rather than $1.99
# We can see that in the file 'data_cleaning_dataset_original.csv' the Duration value in line 9 is out of the range of most of the other values in the list of data, so we would want to change it so that it is more like the other data

# Replacing Values -
# One way to fix an incorrect piece of data is to replace it with an accurate piece of data
# If we wanted to fix the incorrect piece of data in line 9 (mentioned above), we could use the loc() method to locate and change the value of that cell:
data_frame.loc[8, 'Duration'] = 45  # 450 was probably a typo rather than putting 45 in, so we can correct that mistake by replacing the value in the cell

# If we had multiple values that are incorrect, and we would like to compare it to another value in the data frame, we can do that:
for i in data_frame.index:  # Note that you have to call the dataframe.index method on the data frame to give Python the index of the current cell in the loop
    if data_frame.loc[i, 'Pulse'] > data_frame.loc[i, 'Maxpulse']:
        data_frame.loc[i, 'Pulse'] = data_frame.loc[i, 'Maxpulse'] - 15
# Changes all cells where the Pulse value is larger than the Maxpulse value in the same row to whatever Maxpulse is minus 15

# Removing Rows -
# Another way to rectify an incorrect value(s) in a dataset is to remove the row with the incorrect data. This will probably be more helpful for large data frames that the user cannot search through manually and change all the values with
for i in data_frame.index:
    if data_frame.loc[i, 'Duration'] > 60:  # Removes all rows where the Duration value is more than 60
        data_frame.drop(i, inplace=True)

# DUPLICATE DATA:
# Duplicate data is data that has been repeated multiple times. This can confuse a person who is reading the data frame as well as an interpreter like Python trying to manipulate the data frame.
# In file 'data_cleaning_dataset_original.csv', lines 13 and 14 have the same data twice in a row. We do not need the same data twice, so we have to get rid of it somehow.

# Finding Duplicates Using the .duplicated() method -
# To find duplicate values in your data frame, Pandas has a useful method that you can use on a Pandas data frame that returns True or False for every row and whether it has a duplicate value or not:
print(data_frame.duplicated())  # This will return a list of True's and False's depending on whether there are duplicate values or not. We expect two True returns on lines 13 and 14

# Removing Duplicates Using the .drop_duplicates() method -
# Now that we know where the duplicate values are, we can remove them from the data frame using another useful Pandas method called .drop_duplicates():
data_frame.drop_duplicates(inplace=True)  # This automatically removes all duplicate values that Pandas detects. The inplace=True prevents Pandas from returning a new data frame and instead keeps all the changes in the original data frame
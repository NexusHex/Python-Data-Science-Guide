import numpy as np

# Filtering an array means limiting the amount of elements from a list that are shown based on a certain condition
# Example:
# arr = np.arange(0,51)
# new_arr = np.array([])
# for element in arr:
#   if element >= 30:
#       new_arr.append(arr)
#   else:
#       pass
# print(new_arr)

# This example creates an array with numbers ranging from 0 to 50, an empty array, and then checks each element within the list to see if it is more
# than or equal to 30. If the element is, then it is appended to the empty array. The empty array should end up being filled with all the numbers from
# 30 to 50, since all those numbers are greater than or equal to 30

# PART I.I - FILTERING ARRAYS USING BOOLEAN LISTS:
# One of the easiest ways to filter a Numpy array is to create a list with boolean values and creating a new array using the original array and the
# index of the boolean value list:
arr = np.array([41,42,43,44])
x = [True, False, True, False]  # True = The value will be shown. False = The value will not be shown

new_arr = arr[x]  # We create a new array using the original array and the boolean values so Numpy can tell which values to include and which ones to drop
print(new_arr)

# PART I.II - FILTERING USING BOOLEANS AND FOR LOOPS:
# We can use a for loop to cycle through the values of an array, maybe if it is too big for us to do manually:
large_arr = np.arange(101)  # Make an array with numbers going from 0 to 100 (check 'Numpy Methods' if you don't understand this function)
filter_arr = []  # Create an empty array for our boolean values

for element in large_arr:  # For each number in 'large_arr':
    if element >= 50:  # If the number is more than or equal to 50:
        filter_arr.append(True)  # Append True to the 'filter_arr' list
    else:  # If the number is less than 50:
        filter_arr.append(False)  # Append False to the 'filter_arr' list

filtered_large_arr = large_arr[filter_arr]  # Create new array using original array with the filter boolean list as its index, so that the array only puts out the values that are more than or equal to 50

print(large_arr)
print(filtered_large_arr)

# Here is another example that filters an array to only have even numbers:
evens_and_odds = np.arange(101)  # Numbers 0 to 100
even_filter = []

for element in evens_and_odds:
    if element % 2 == 0:  # If dividing the number by 2 leaves a remainder of 0
        even_filter.append(True)
    else:
        even_filter.append(False)

just_evens = evens_and_odds[even_filter]

print(evens_and_odds)
print(just_evens)

# PART II - CREATING A FILTERED ARRAY DIRECTLY FROM AN ARRAY:
# Instead of wasting time and making whole loops just to filter an array, Numpy allows us to create a filtered array directly from the original array:
unfiltered_arr = np.arange(41)  # Numbers 0 to 40
arr_filter = unfiltered_arr >= 20  # filtered_arr = all values of unfiltered_arr that are more than or equal to 20

filtered_arr = unfiltered_arr[arr_filter]  # Same thing we've been doing for the past couple of examples...

print(unfiltered_arr)
print(filtered_arr)
# You can tell that this method saves us time since it is much shorter than the last few methods we've been using.
# Of course, you can still do filtering with the for loop method or by manually creating a list, but this is the fastest way :)

# Like last part, an example of just returning even numbers:
x = np.arange(71)  # Numbers 0 to 70
y = x % 2 == 0  # y = all vals of x that have remainder of 0 when divided by 2

z = x[y]

print(x)
print(z)
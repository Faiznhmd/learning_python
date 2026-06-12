# Sets are used to store multiple items in a single variable.
# myset = {"apple", "banana", "cherry"}
# Set items are unchangeable, but you can remove items and add new items
# Sets are unordered, so you cannot be sure in which order the items will appear.
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Unordered means that the items in a set do not have a defined order.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


# True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

# The values False and 0 are considered the same value in sets, and are treated as duplicates:

# False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)



# Get the number of items in a set:  len

thisset = {"apple", "banana", "cherry"}

print(len(thisset))


# Set Items - Data Types
# Set items can be of any data type:

# Example
# String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
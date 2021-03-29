"""
File: bubble_sort.py 
Author: COMP 120 class
Date: April 6, 2021
Description: Has function to bubble sort a list.
"""


def bubble_sort(items):
    """
    Sort items from smallest to largest
    using bubble sort.
    """
    n = len(items)
    for p in range(n - 1):
        # make a pass through the data, starting at index 0
        for i in range(n - 1 - p):
            if items[i] > items[i + 1]:
                items[i], items[i+1] = items[i+1], items[i]

def bubble_sort_b(items):
    """
    Sort items from smallest to largest
    using bubble sort.
    Instead of bubbling the biggest (remaining) value to the 
    right, this version bubbles the smallest (remaining) value
    to the left.
    """
    pass  # replace this

items = [77, 94, 4, 12, 33, 54, 66, 19, 8, 83]
items_copy = items
print("Original list")
print(items)

# Sort with original bubble sort
bubble_sort(items)

# Sort with revised bubble sort
bubble_sort_b(items_copy)

# Make sure correct
if items == items_copy:
    print("Correct.  Nice job")
    print("Your sorted list")
    print(items_copy)
else:
    print("Incorrect.  Should be")
    print(items)
    print("Your code produces")
    print(items_copy)
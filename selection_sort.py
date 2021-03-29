"""
File: selection_sort.py 
Author: COMP 120 class
Date: April 6, 2021
Description: Has function for selection sort.
"""
def selection_sort(ar):
    """ 
    Sorts the items in the list ar from smallest to largest, using
    selection sort.
    Selection sort finds the smallest value in the list, and swaps
    it into the first position.
    Then it finds the next smallest value in the list, and swaps it
    int the second position.
    This is continued, until the second largest value is swapped into
    the second last position.    
    """
    n = len(ar)
    for index in range(n - 1):
        index_smallest = index
        for j in range(index + 1, n):
            if ar[j] < ar[index_smallest]:
                index_smallest = j
        if index_smallest != index:
            ar[index_smallest], ar[index] = ar[index], ar[index_smallest]

def selection_sort_b(ar):
    """ 
    Sorts the items in the list ar from smallest to largest, using
    selection sort.  
    This is the same as the above version of selection_sort, but
    in this version, you find the largest values, and swap them into 
    their correct locations.  So,
    Find the largest value in the list, and swap
    it into the last position.
    Then, finds the next largest value in the list, and swap it
    int the second last position.
    This is continued, until the second smallest value is swapped into
    the second position.    
    """
    pass # replace this

items = [77, 94, 4, 12, 33, 54, 66, 19, 8, 83]
items_copy = items
print("Original list")
print(items)

# Sort with original selection sort
selection_sort(items)

# Sort with revised selection sort
selection_sort_b(items_copy)

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
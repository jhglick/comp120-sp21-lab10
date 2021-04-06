"""
File: mergesort.py 
Author: COMP 120 class
Date: March 23, 2021
Description: Has functions to merge sort a list.
"""

def merge_sort(items):
    """
    Sort items from smallest to largest
    using merge sort.
    """
    temp_list = [0] * len(items)
    merge_sort_recursive(items, temp_list, 0, len(items) - 1)

def merge_sort_recursive(items, temp_list, low, high):
    """
    Sort items[low:high+1] from smallest to largest
    using merge sort
    """
    if low >= high:
        return
    else:
        mid = (low + high) // 2
        merge_sort_recursive(items, temp_list, low, mid)
        merge_sort_recursive(items, temp_list, mid + 1, high)
        merge(items, temp_list, low, mid, high)

def merge(items, temp_list, low, mid, high):
    """
    Merge already sorted items[low:mid+1] and items[mid+1:high+1]
    into temp_list, and then copy back into items[low:high+1]
    """
    i1 = low
    i2 = mid + 1
    i_temp = low

    # While items in both parts remain to be compared,
    # compare them and copy the smaller value in temp_list.
    while i1 <= mid and i2 <= high:
        if items[i1] <= items[i2]:
            temp_list[i_temp] = items[i1]
            i1 += 1
        else:
            temp_list[i_temp] = items[i2]
            i2 += 1
        i_temp += 1

    # Copy remaining values from the left part.
    while i1 <= mid:
        temp_list[i_temp] = items[i1]
        i1 += 1
        i_temp += 1

    # Copy the remaining values from the right part.
    while i2 <= high:
        temp_list[i_temp] = items[i2]
        i2 += 1
        i_temp += 1

    # Copy values from temp_list back to items.
    for i in range(low, high + 1):
        items[i] = temp_list[i]

def merge_sort_b(items):
    """
    Sort items from smallest to largest
    using merge sort.  This version uses
    the merge_b function.
    """
    temp_list = [0] * len(items)
    merge_sort_recursive_b(items, temp_list, 0, len(items) - 1)

def merge_sort_recursive_b(items, temp_list, low, high):
    """
    Sort items[low:high+1] from smallest to largest
    using merge sort.

    This version uses the merge_b function.
    """
    if low >= high:
        return
    else:
        mid = (low + high) // 2
        merge_sort_recursive_b(items, temp_list, low, mid)
        merge_sort_recursive_b(items, temp_list, mid + 1, high)
        merge_b(items, temp_list, low, mid, high)

def merge_b(items, temp_list, low, mid, high):
    """
    Merge already sorted items[low:mid] and items[mid+1:high+1]
    into temp_list, and then copy back into items[low:high+1]

    In this version, you should merge the values from the largest
    to the smallest value.  So the first value you should copy
    into temp_list is the largest value in either part.
    """
    pass # replace this

items = [77, 94, 4, 12, 33, 54, 66, 19, 8, 83]
items_copy = list(items)
print("Original list")
print(items)

# Sort with original selection sort
merge_sort(items)

# Sort with revised selection sort
merge_sort_b(items_copy)

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

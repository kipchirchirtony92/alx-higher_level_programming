#!/usr/bin/env python3
# Find the peak of an unsorted array

def find_peak(array):
    """ Returns the peak of unsorted array of integers"""
    size = len(array)

    if array == []:
        return None
    elif size == 1:
        return array[0]
    elif size == 2:
        return max(array)

    mid = int(size / 2)

    peak = array[mid]

    if peak > array[mid + 1] and peak > array[mid - 1]:
        return peak
    elif peak <= array[mid - 1]:
        return find_peak(array[:mid])
    else:
        return find_peak(array[mid + 1:])

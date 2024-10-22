# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/131yFwvDI-5_Dj6_lG8k54f4s_83HH_2Y
"""

def find_second_largest_and_smallest(arr):

    unique_arr = list(set(arr))
    unique_arr.sort()


    second_smallest = unique_arr[1]
    second_largest = unique_arr[-2]

    return second_smallest, second_largest


array = [1,2,4,7,7,5]
second_smallest, second_largest = find_second_largest_and_smallest(array)

print(second_smallest)
print(second_largest)
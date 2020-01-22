""""
MERGE SORT ALGORITHM IN PYTHON

Pseudocode:

"""
from typing import List
from math import floor

def mergeSort(arr: List[int]) -> List[int]:
    if len(arr) == 1:
        return arr

    #get middle item of the array rounded down
    mid_index = floor(len(arr) / 2)

    #create a variable for items on left side
    left_half = arr[0:mid_index]

    #create variable for right side
    right_half = arr[mid_index:]

    return merge(
        mergeSort(left_half),
        mergeSort(right_half)
    )
    
def merge(left: List[int], right: List[int]) -> List[int]:
    left_index = 0
    right_index = 0
    merged_list = []
     
    
    while (left_index < len(left) and right_index < len(right)):
        if (left[left_index] < right[right_index]):
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1

    return merged_list + left[left_index:] + right[right_index:] 


#test case and output for the merge sort algorithm
test_array = [1,7,3,9,12,17,32,5,8,13,11] #answer = [1,3,5,7,8,9,11,12,13,17,32]
print(mergeSort(test_array))

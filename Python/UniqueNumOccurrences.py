"""
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

 

Example 1:
----------

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
----------

Input: arr = [1,2]
Output: false

Example 3:
----------
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true



ALTERNATE SOLUTION
-------------------

Python gives all of hte functions to perform a solution for the problem above. 
this is a pythonic way of solving the problem.

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        numOccur = Counter(occur for key, occur in counter.items())
        return all(times == 1 for freq, times in numOccur.items())

"""
#although the algorithmbelow is slower, it is more descriptive of how the algorithm works. 

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        _map = {}

        #iterate through array and if the number is not in the map, add it to the map, if it is then incrmeent its value
        for num in arr:
            if num not in _map:
                _map[num] = 1
            else:
                _map[num] += 1

        #if the length of the values array is the same as the set of the values, then there are no duplicates
        if len(_map) == len(set(_map.values())):
            return True
        else:
            return False



#Testing the solution
test_arr1 = [1,2,2,1,1,3]
test_arr2 = [1,2]
test_arr3 = [-3,0,1,-3,1,1,1,-3,10,0]

print(Solution().uniqueOccurrences(test_arr3))
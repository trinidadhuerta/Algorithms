"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

NOTE:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even

Example 1:
----------

Input: [1,2,3,3]
Output: 3

Example 2:
----------

Input: [2,1,2,5,3,2]
Output: 2

Example 3:
----------

Input: [5,1,5,2,5,3,5,4]
Output: 5
 


"""

#Since we know that the ony repeated element will be the return value, we can map the values weve seen
# and if the value being checked is already in the map just return it. 

from typing import List

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        _map = {}
        
        for elem in A:
            if elem not in _map:
                _map[elem] = 1
            else:
                return elem
        return -1 #error

#Test solution
test_arr1 = [1,2,3,3]
test_arr2 = [2,1,2,5,3,2]
test_arr3 = [5,1,5,2,5,3,5,4]

print(Solution().repeatedNTimes(test_arr3))
"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  
An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

 
Example 1:
----------

Input: [1,2,2,3]
Output: true

Example 2:
----------

Input: [6,5,4,4]
Output: true

Example 3:
----------

Input: [1,3,2]
Output: false

Example 4:
----------

Input: [1,2,4,5]
Output: true

Example 5:
----------

Input: [1,1,1]
Output: true
 

Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
"""
from typing import List

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        mono_dec = True
        mono_inc = True
        
        for num in range(len(A) - 1):
            if A[num] < A[num+1]:
                mono_inc = False
            if A[num] > A[num+1]:
                mono_dec = False
        
        if mono_dec or mono_inc:
            return True
        else:
            return False

#Testing solution
t1 = [1,2,2,3] #true
t2 = [6,5,4,4] #true
t3 = [1,3,2] #false
t4 = [1,2,4,5] #true
t5 = [1,1,1] #true

print(Solution().isMonotonic(t2))
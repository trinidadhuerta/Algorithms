

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
import sys
from typing import List

class Solution:

    test_nums1 = [2,7,11,15] #target = 9
    test_nums2 = [3,6,7,1,9,11,18,13,10] #target = 31
    test_nums3 = [12,19,18,23,1,3,9,13,95] #target = 96

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = None

        print(f"Searching for numbers that add up to {target} in the list {nums}")

        """
        BRUTE FORCE SOLUTION
        for the brute force solution we can go through each element of the array and the compare it to the following elements

        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j) and (nums[i] + nums[j]) == target:
                    print(f"two numbers found at indices {i} and {j}")
                    print(f"the numbers are {nums[i]} and {nums[j]}")
                    return [i,j]
                else:
                    continue
        
        """

        """
        O(N) SOLUTION
        """
        
        return result

    def printResult(self):
        print(twoSum(test_nums1, 9))



#test the code
test = Solution()
print(test.twoSum(test.test_nums1,9))
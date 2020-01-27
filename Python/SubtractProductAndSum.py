"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Example 1:
----------

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

Example 2:
-----------

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21

"""

from functools import reduce
import operator

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        #create a list by mapping the int() function to each digit to convert each char into its own digit
        A = list(map(int,str(n)))
        #reduce gets the product of the elements in the list
        #sum() adds oall of the elements in the list
        return reduce(operator.mul, A) - sum(A)

test_num1 = 234
test_num2 = 4421

print(Solution().subtractProductAndSum(234))
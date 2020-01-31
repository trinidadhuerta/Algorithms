"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

NOTE:

The boundaries of each input argument are 1 <= left <= right <= 10000.

Example 1:
----------
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

"""
from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        self_div_list = []

        for num in range(left,right+1):
            is_self_div = True
            temp_num = num

            #check each number for division by each of its digits
            while temp_num > 1:

                divisor = int(temp_num % 10)
                temp_num = int(temp_num / 10)
                
                if divisor == 0:
                    is_self_div = False
                    continue

                if num % divisor != 0:
                    is_self_div = False

            if  is_self_div:
                self_div_list.append(num)

        return self_div_list
                
            
            

print(Solution().selfDividingNumbers(99,101))
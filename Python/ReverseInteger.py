"""
Given a 32-bit signed integer, reverse the digits of the integer.

Example 1:
input: 123
output: 321

Example 2:
input: -123
output: -321

Example 3:
input: 120
output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

class Solution:
    def reverse(self, x: int) -> int:
        num_in = x
        num_out = 0

        while num_in != 0:
            pop = num_in%10
            num_in = int(num_in / 10)
            num_out = int((num_out*10) + pop)
            
            print(f"number popped = {pop}")
            print(f"next number to check = {num_in}")
            print(f"current output = {num_out}")
        
        return 0

print("Starting the check...")
Solution().reverse(12345)

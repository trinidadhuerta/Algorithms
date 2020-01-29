"""
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Constraints:

1 <= num <= 10^4
num's digits are 6 or 9.


Example 1:
----------

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666. 
The maximum number is 9969.

Example 2:
-----------

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.


Example 3:
----------

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.



SOLUTION 1:
This solution converts the number into a string, checks the character to see if it is a 6.
if it is a 6, it changes it to a 9 and immediately returns the list as an integer

class Solution:
    def maximum69Number (self, num: int) -> int:

        digit_list = list(str(num))
        
        #check each digit, if it is a 6 change it to a 9 and then return the modifed list immediately
        for digit in range(len(digit_list)):
            if digit_list[digit] == '6':
                digit_list[digit] = '9'
                return int("".join(digit_list))
                
        #If no 6 is found, return the original number
        return int("".join(digit_list))
"""
#The following solution works on the integer without first converting it to a string, the runtime is the same at O(log n) BUT
# it is much more efficient because it doesnt need to convert to string  before examinging to digits. 


from typing import List

class Solution:
    def maximum69Number (self, num: int) -> int:
        cur_position = 0
        leftmost_six = -1
        num_copy = num

        while (num_copy > 1):
            #get the digit at the rightmost position
            digit = int(num_copy % 10)

            #reduce the num passed in by factor of 10, increase the position of the leftmost digit
            num_copy = int(num_copy / 10)

            #if the digit is a 6 increment the  cur_position
            if digit == 6:
                leftmost_six = cur_position
            
            cur_position += 1

        #if cur_position is less than 0 then there were no 6 digits found
        if leftmost_six >= 0:
            print(f"Doing the calculation for 3 * 10^{leftmost_six}")
            return num + (3 * 10**leftmost_six) #adding the integer value to the original number
        else:
            return num


#Test the solution
test_num = 9999

print(f"Testing the number: {test_num}")
print(Solution().maximum69Number(test_num))
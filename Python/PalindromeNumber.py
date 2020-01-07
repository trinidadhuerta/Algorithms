"""
Determine whether an integer is a palindrome. 

An integer is a palindrome when it reads the same backward as forward.

Example 1:
input: 121
Output: True


Example 2:
input: -121
Output: False


Example 3:
input: 10
Output: False

---------------------------    SOLUTION USING STRINGS -------------------------

There is a very simple method of converting the number to a string, reversing the string and then comparing the initial string to the new one.
below is the solution if string usage is allowed. 

Class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

"""

#SOLUTION USING NO STRINGS

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_in = x
        rev_num = 0

        if num_in < 0:
            return False
        else:
            while num_in != 0:
                pop = num_in % 10
                num_in = int(num_in / 10)
                rev_num = int((rev_num * 10) + pop)

            if rev_num == x: 
                return True
            else:
                return False

print(Solution().isPalindrome(121))

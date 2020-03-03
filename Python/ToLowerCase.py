"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:
----------

Input: "Hello"
Output: "hello"

Example 2:
----------

Input: "here"
Output: "here"

Example 3:
----------

Input: "LOVELY"
Output: "lovely"
"""
class Solution:
    def toLowerCase(self, str: str) -> str:
        ls = ""

        for char in str:
            if 65 <= ord(char) <= 90:
                ls += chr(ord(char) + 32)
            else:
                ls += char
        
        return ls

#Testing solution
str1 = "Hello"
str2 = "here"
str3 = "LOVELY"

print(Solution().toLowerCase(str3))
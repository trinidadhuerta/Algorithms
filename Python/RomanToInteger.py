"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I            1
V            5
X            10
L            50
C            100
D            500
M            1000


For example, two is written as II in Roman numeral, just two one's added together. 
Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.


Example 1:
input: III
output: 3

Example 2:
input: IV
output: 4

Example 3:
input: IX
output: 9 

Example 4:
input: LVIII
output: 58

Example 5:
input: MCMXCIV
output: 1994

"""

class Solution:
    def romanToInt(self, s: str) -> int:
        #First create a map for easy key value pair lookups
        map = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        prev_char = "" #holds the previous character read
        total = 0 #total

        #work backwards on the string 
        for char in reversed(s):
            if char in map:
                if prev_char in map and map[prev_char] > map[char]: #if the previous character value is greater than the one currently being checked
                    total -= map[char]
                else:
                    total += map[char]

            prev_char = char
        return total


print(Solution().romanToInt("MCMXCIV"))

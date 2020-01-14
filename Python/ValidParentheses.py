"""

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
input: "()"
output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true


The solution below uses a List to simulate the stack data structure. 

if the parentheses that is read is an opening brace, then it places it into the stack
if the parentheses that is a read is a closing brace, then
    1. checks if the stack is currently empty
    2. checks if the character is a valid character
    3. cheks if the elemtn at the top of the stack is the opening brace for the character read in
        4. if it is, then remove the last elemetn from the stack 
        5. if it isnt then push the character at the top of the stack 

"""
class Solution:


    def isValid(self, s: str) -> bool:
        
        map = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []

        #cannot be an odd number of characters in the string
        if (len(s) % 2) > 0:
            return False

        
        for char in s:
            if stack and (char in map and stack[-1] == map[char]):
                stack.pop()
            else:
                stack.append(char)

        return not stack


#TESTING ALGORITHM
test_string1 = "()" #true
test_string2 = "()[]{}" #true
test_string3 = "(]" #false
test_string4 = "([)]" #false
test_string5 = "{{}}" #true
test_string6 = "({[({})]}{}())" # true

print(f"Now testing the string: {test_string6}")
print(Solution().isValid(test_string6))




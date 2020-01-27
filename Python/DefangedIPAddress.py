"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:
----------

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"


Example 2:
----------

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"



NOTE: for this solution we could have easily used the "replace" functionality of python lists such as below

return address.replace(".", "[.]")

this would have replaced the instances of a period with "[.]" 
but for the purposes of learning, we have skipped this a solution even though it is faster. 
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        ls = []

        for char in address:
            if char == ".":
                ls.append("[.]")
            else:
                ls.append(char)
        
        return "".join(ls)

address1 = "1.1.1.1"
address2 = "255.100.50.0"

print(Solution().defangIPaddr(address2))
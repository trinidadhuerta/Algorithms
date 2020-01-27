"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

J = jewels
S = stones

The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:
Input: J = "z", S = "ZZ"
Output: 0

BRUTE FORCE:
The brute force algorithm will take each jewel in the jewel array and cross reference each stone.
if the jewel letter is found in the stones, then it will increent a counter by 1. 

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0

        for jewel in J:
            for stone in S:
                if jewel == stone:
                    counter += 1
        return counter

the problem with this algorithm is that for each jewel it has to iterate through the entire stone array each time, complexity then is N^2.
the easiest thing to do then would be to aim for O(N) time by only iterating through the stones array once.
"""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0

        for stone in S:
            if stone in J:
                counter += 1 

        return counter



J_string = "aA"
S_string = "aAAbbbb"

print(Solution().numJewelsInStones(J_string, S_string))

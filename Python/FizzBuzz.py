"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
For numbers which are multiples of both three and five output “FizzBuzz”.

EXAMPLE:
--------

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]


Alternate Solution:
------------------
the solution below is slower overall when run BUT it does bypass the need for the extra modulus operations by setting true or false flags for a number.
it then only does comparisons on the number based on those boolean values rather than running an extra mod3 and mod5 operation.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        return_list = []

        for i in range(1,n+1):
            divis_by_three = False
            divis_by_five = False

            #Do a pre-check on the number to see if it can be divided by 5 or 3
            if i % 3 == 0:
                divis_by_three = True
            if i % 5 == 0:
                divis_by_five = True

            #depending on the boolean values above, set the value of the string
            if divis_by_five and divis_by_three:
                return_list.append("FizzBuzz")
            elif divis_by_five:
                return_list.append("Buzz")
            elif divis_by_three:
                return_list.append("Fizz")
            else:
                return_list.append(f"{i}")
                
        return return_list
"""
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        return_list = []

        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                return_list.append("FizzBuzz")
            elif i % 3 == 0:
                return_list.append("Fizz")
            elif i % 5 == 0:
                return_list.append("Buzz")
            else:
                return_list.append(f"{i}")

        return return_list


#Testing Solution
print(Solution().fizzBuzz(15))

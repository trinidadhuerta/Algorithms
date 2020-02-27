"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
Check if these points make a straight line in the XY plane.



Example 1:
----------

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
----------

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Example 3:
----------

input: coordiantes = [[-1,1],[-6,-4],[-6,2],[2,0],[-1,-2],[0,-4]]

Constraints:
------------

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.

"""
from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        if len(coordinates) == 2:
            return True
        
        rise = coordinates[1][1] - coordinates[0][1]
        run = coordinates[1][0] - coordinates[0][0]
        
        if run == 0:
            slope = "undefined"
        else:
            slope = rise / run


        for i in range(1, len(coordinates) - 1):
            
            cur_rise = coordinates[i + 1][1] - coordinates[i][1]
            cur_run = coordinates[i + 1][0] - coordinates[i][0]
        
            if cur_run == 0:
                cur_slope = "undefined"
            else:
                cur_slope = cur_rise / cur_run

            if slope != cur_slope:
                return False
        
        return True

c1 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
c2 = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
c3 = [[-1,1],[-6,-4],[-6,2],[2,0],[-1,-2],[0,-4]]

print(Solution().checkStraightLine(c1))
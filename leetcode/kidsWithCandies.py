from leetcode_runner import LeetCode, TestCase, Args
from typing import *

problem = '''
Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [True,True,True,False,True] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

Example 2:

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [True,False,False,False,False] 
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

Example 3:

Input: candies = [12,1,12], extraCandies = 10
Output: [True,False,True]

Constraints:

    n == candies.length
    2 <= n <= 100
    1 <= candies[i] <= 100
    1 <= extraCandies <= 50
'''

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        solution = []
        # Get highest number of candies from list
        maxCandies = max(candies)
        for candy in candies:
            if candy + extraCandies >= maxCandies:
                solution.append(True)
            else:
                solution.append(False)
        return solution
       
LeetCode(problem, Solution).check()
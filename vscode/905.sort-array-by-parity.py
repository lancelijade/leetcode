#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
from collections import deque

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        r = deque()
        for n in nums:
            if n % 2 != 0:
                r.append(n)
            else:
                r.appendleft(n)
                
        return r

# @lc code=end


#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
from sortedcontainers import SortedSet


class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nn = SortedSet(nums)
        if len(nn)>=3: return nn[-3]
        return nn[-1]

# @lc code=end

nums = [3,2,1]
nums = [2,2,3,1]
nums = [1,2]

so = Solution()
r = so.thirdMax(nums)
print(r)
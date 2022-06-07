#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        c = Counter(nums)
        return c.most_common()[:-2:-1][0][0]
        
        
# @lc code=end

nums = [4,1,2,1,2]

so = Solution()
r = so.singleNumber(nums)
print(r)
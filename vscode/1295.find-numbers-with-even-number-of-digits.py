#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
from math import log10

class Solution2:
    def findNumbers(self, nums: list[int]) -> int:
        r = 0
        for n in nums:
            if int(log10(n))%2 == 1: r += 1
        return r
        
class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        r = 0
        for n in nums:
            if 10<=n<=99 or 1000<=n<=9999 or 100000==n:
                r += 1
        return r

# @lc code=end

nums = [12,345,2,6,7896]
#nums = [555,901,482,1771]

so = Solution()
r = so.findNumbers(nums)
print(r)
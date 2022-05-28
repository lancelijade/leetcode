#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        s = int(n * (n + 1) / 2)
        return s - sum(nums)
        
# @lc code=end

nums = [9,6,4,2,3,5,7,0,1]
#nums = [3,0,1]

so = Solution()
r = so.missingNumber(nums)
print(r)
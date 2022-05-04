#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        r = 0
        cur = -1
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                r = max(r, i-cur)
            else:
                cur = i
            i += 1
        return r
        
# @lc code=end

nums = [1,1,0,1,1,1]
nums = [1,0,1,1,0,1]

so = Solution()
r = so.findMaxConsecutiveOnes(nums)
print(r)
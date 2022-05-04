#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i, n in enumerate(nums):
            nums[i] = n*n
        nums.sort()
        return nums
        
        
# @lc code=end

nums = [-4,-1,0,3,10]

so = Solution()
r = so.sortedSquares(nums)
print(r)
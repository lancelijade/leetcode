#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        le = len(nums)
        for i in range(le):
            for j in range(i + 1, le):
                if nums[i] + nums[j] == target: return [i, j]
        
# @lc code=end

nums = [2,7,11,15]
target = 9

nums = [3,3]
target = 6

so = Solution()
r = so.twoSum(nums, target)
print(r)
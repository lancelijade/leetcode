#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        r = [nums[0]]
        for i in range(1, len(nums)):
            r.append(nums[i]+r[i-1])
        return r


# @lc code=end

nums = [1,2,3,4]
nums = [1,1,1,1,1]
nums = [3,1,2,10,1]

so = Solution()
r = so.runningSum(nums)
print(r)
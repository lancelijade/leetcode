#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        c = 0
        while i<len(nums):
            if nums[i] != val:
                nums[c] = nums[i]
                c += 1
            i += 1
        return c

        
# @lc code=end

nums = [3,2,2,3]
val = 3

nums = [0,1,2,2,3,0,4,2]
val = 2

so = Solution()
r = so.removeElement(nums, val)
print(r, nums)
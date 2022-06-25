#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        c = []
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                c.append(i)
                if len(c) >= 2:
                    return False
        
        # make sure i-1 < i+1 or i < i+2
        if len(c) > 0:
            i = c[0]
            if i == 0 or i == len(nums)-2:
                return True
            elif nums[i-1] <= nums[i+1] or nums[i] < nums[i+2]:
                return True

            return False

        return True

        
# @lc code=end

nums = [4,2,3]
#nums = [4,2,1]
nums = [3,4,2,3]
#nums = [-1,4,2,3]
#nums = [5,7,1,8]
nums = [1,2,4,5,3]

so = Solution()
r = so.checkPossibility(nums)
print(r)
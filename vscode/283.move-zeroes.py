#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        le = len(nums)
        if le==1: return

        total = nums.count(0)
        tail = 0
        for i in range(le-1, -1, -1):
            if nums[i] == 0: tail += 1
            else: break
        if tail == total: return

        for i in range(total-tail):
            nums.remove(0)
            nums.append(0)

        
# @lc code=end

nums = [0,1,0,3,12,0,0,0,0]

so = Solution()
so.moveZeroes(nums)
print(nums)
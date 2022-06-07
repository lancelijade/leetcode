#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        a = set(nums)
        return len(a) != len(nums)

        
# @lc code=end

nums = [1,1,1,3,3,4,3,2,4,2]

so = Solution()
r = so.containsDuplicate(nums)
print(r)
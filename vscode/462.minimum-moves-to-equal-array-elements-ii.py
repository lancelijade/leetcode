#
# @lc app=leetcode id=462 lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
#

# @lc code=start
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        r = 0
        for n in nums:
            r += abs(n - nums[len(nums) // 2])
        return r

        
# @lc code=end

nums = [1,10,2,9]
nums = [1,0,0,8,6]


so = Solution()
r = so.minMoves2(nums)
print(r)
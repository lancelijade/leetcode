#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d = defaultdict(int)

        for i, n in enumerate(nums):
            if n in d and i - d[n] <= k:
                return True
            else:
                d[n] = i
        
        return False

        
# @lc code=end

nums = [1,2,3,1]
k = 3

nums = [1,0,1,1]
k = 1

nums = [1,2,3,1,2,3]
k = 2

so = Solution()
r = so.containsNearbyDuplicate(nums, k)
print(r)
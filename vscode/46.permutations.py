#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from collections import deque


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        q = deque()
        q.append([])
        while len(q[0]) != len(nums):
            cur = q.popleft()
            for n in nums:
                if n not in cur:
                    q.append(cur + [n])
        return q

        
# @lc code=end

nums = [1,2,3]

so = Solution()
r = so.permute(nums)
print(r)
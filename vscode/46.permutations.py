#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from collections import deque


class Solution:
    def permute1(self, nums: list[int]) -> list[list[int]]:
        q = deque()
        q.append([])
        while len(q[0]) != len(nums):
            cur = q.popleft()
            for n in nums:
                if n not in cur:
                    q.append(cur + [n])
        return q


    def permute(self, nums: list[int]) -> list[list[int]]:
        
        def helper(o: list[int]):
            if len(o) == len(nums):
                return [o]
            
            r = []
            for n in nums:
                if n not in o:
                    r += helper(o + [n])

            return r

        return helper([])


        
# @lc code=end

nums = [1,2,3]

so = Solution()
r = so.permute(nums)
print(r)
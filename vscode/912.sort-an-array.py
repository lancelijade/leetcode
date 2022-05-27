#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
from collections import deque


class Solution:

    def mergesort(self, a, b):
        return sorted(a + b)

    def sortArray(self, nums: list[int]) -> list[int]:
        q = deque()
        for x in nums:
            q.append([x])
            
        while len(q) > 1:
            a = q.popleft()
            b = q.popleft()
            q.append(self.mergesort(a, b))
        return q[0]

        
# @lc code=end

nums = [5,2,3,1]


so = Solution()
r = so.sortArray(nums)
print(r)
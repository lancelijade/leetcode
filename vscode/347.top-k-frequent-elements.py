#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
import heapq
from typing import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        if k == len(nums): return nums

        c = Counter(nums)

        #return sorted(c.keys(), key=c.get, reverse=True)[:k]
        return heapq.nlargest(k, c.keys(), c.get)
        
# @lc code=end

nums = [1,1,1,2,2,3]
k = 2

so = Solution()
r = so.topKFrequent(nums, k)
print(r)
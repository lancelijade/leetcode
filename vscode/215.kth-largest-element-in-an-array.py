#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq

class Solution:
    def findKthLargest2(self, nums: list[int], k: int) -> int:
        nn = [-x for x in nums]
        heapq.heapify(nn)
        for i in range(k):
            r = heapq.heappop(nn)
        return -r

    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        r = heapq.nlargest(k, nums)
        return r[-1]

# @lc code=end

nums = [3,2,1,5,6,4]
k = 2

nums = [3,2,3,1,2,4,5,5,6]
k = 4

so = Solution()
r = so.findKthLargest(nums, k)
print(r)

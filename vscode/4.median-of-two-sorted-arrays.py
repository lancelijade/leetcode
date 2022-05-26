#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
import heapq


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        e1 = len(nums1)
        e2 = len(nums2)
        total = e1 + e2

        h = heapq.merge(nums1, nums2)

        if total % 2 == 0:
            r = heapq.nlargest(total//2+1, h)[-2:]
            return sum(r)/2
        else:
            r = heapq.nlargest(total//2+1, h)[-1]
            return r
        


        
# @lc code=end

nums1 = [1,2]
nums2 = [3,4]

so = Solution()
r = so.findMedianSortedArrays(nums1, nums2)
print(r)
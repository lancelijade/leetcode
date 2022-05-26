#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
import heapq


class Solution:
    def findMedianSortedArrays2(self, nums1: list[int], nums2: list[int]) -> float:
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
        
        
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total = len(nums1) + len(nums2)

        a = sorted(nums1 + nums2)
        if total % 2 == 0:
            return (a[total//2-1] + a[total//2])/2
        else:
            return a[total//2]
        
        """
        2094/2094 cases passed (94 ms)
        Your runtime beats 91.41 % of python3 submissions
        Your memory usage beats 68.33 % of python3 submissions (14.1 MB)
        """        

        
# @lc code=end

nums1 = [1,2]
nums2 = [3,4,5]

so = Solution()
r = so.findMedianSortedArrays(nums1, nums2)
print(r)
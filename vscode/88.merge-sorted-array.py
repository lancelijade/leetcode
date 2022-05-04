#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m+n-1
        mc = m - 1
        nc = n - 1
        while i>=0:
            if mc>=0 and nc>=0:
                if nums1[mc]>nums2[nc]:
                    nums1[i] = nums1[mc]
                    mc -= 1
                else:
                    nums1[i] = nums2[nc]
                    nc -= 1
            elif mc<0 and nc>=0:
                nums1[i] = nums2[nc]
                nc -= 1
            elif nc<0 and mc>=0:
                nums1[i] = nums1[mc]
                mc -= 1                
            i -= 1
        
# @lc code=end

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

nums1 = [1]
m = 1
nums2 = []
n = 0


so = Solution()
so.merge(nums1, m, nums2, n)
print(nums1)
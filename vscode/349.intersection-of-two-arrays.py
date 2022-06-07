#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))

        
# @lc code=end

nums1 = [1,2,2,1]
nums2 = [2,2]

so = Solution()
r = so.intersection(nums1, nums2)
print(r)
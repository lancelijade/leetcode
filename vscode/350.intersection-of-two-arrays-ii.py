#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
from functools import cache

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        @cache
        def lcs(i, j):
            #print(l1, l2, i, j)
            if i==0 or j==0:
                return []
            elif l1[i-1] == l2[j-1]:
                return lcs(i-1, j-1) + [l1[i-1]]
            else:
                r1 = lcs(i-1, j)
                r2 = lcs(i, j-1)
                if len(r1) > len(r2):
                    return r1
                else:
                    return r2

        l1 = sorted(nums1)
        l2 = sorted(nums2)
        return lcs(len(nums1), len(nums2))

        
# @lc code=end

nums1 = [1,2,2,1]
nums2 = [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

nums1 = [2,1]
nums2 = [1,2]

nums1 = [61,24,20,58,95,53,17,32,45,85,70,20,83,62,35,89,5,95,12,86,58,77,30,64,46,13,5,92,67,40,20,38,31,18,89,85,7,30,67,34,62,35,47,98,3,41,53,26,66,40,54,44,57,46,70,60,4,63,82,42,65,59,17,98,29,72,1,96,82,66,98,6,92,31,43,81,88,60,10,55,66,82,0,79,11,81]
nums2 = [5,25,4,39,57,49,93,79,7,8,49,89,2,7,73,88,45,15,34,92,84,38,85,34,16,6,99,0,2,36,68,52,73,50,77,44,61,48]

so = Solution()
r = so.intersect(nums1, nums2)
print(r)
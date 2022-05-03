#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        nums1 = nums.copy()
        nums1.sort()
        #print(nums1)

        le = len(nums)

        i = 0
        while i<le:
            if nums[i] == nums1[i]: i += 1
            else: break;
        if i==le: return 0
        #print(i)

        j = le-1
        while j>=0:
            if nums[j] == nums1[j]: j -= 1
            else: break;
        #print(j)

        return j-i+1

        
# @lc code=end

nums = [2,6,4,8,10,9,15]
nums = [3,2,1,12]

so = Solution()
r = so.findUnsortedSubarray(nums)
print(r)
#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        s = []
        for n in nums:
            i = bisect_left(s, n)
            if i == len(s):
                s.append(n)
            else:
                s[i] = n
        return len(s)

        
# @lc code=end

nums = [0,1,0,3,2,3]
nums = [7,7,7,7,7,7,7]

so = Solution()
r = so.lengthOfLIS(nums)
print(r)
#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        c = heights.copy()
        c.sort()
        r = 0
        for i in range(len(heights)):
            if c[i] != heights[i]: r += 1
        return r
        
# @lc code=end

heights = [1,1,4,2,1,3]


so = Solution()
r = so.heightChecker(heights)
print(r)
#
# @lc app=leetcode id=1689 lang=python3
#
# [1689] Partitioning Into Minimum Number Of Deci-Binary Numbers
#

# @lc code=start
class Solution:
    def minPartitions(self, n: str) -> int:
        return max(n)


        
# @lc code=end

n = "27346209830709182346"

so = Solution()
r = so.minPartitions(n)
print(r)
#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
from collections import defaultdict


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        if len(triangle) == 1: return triangle[0][0]

        dp = [[] for _ in range(len(triangle))]

        dp[0] = [triangle[0][0]]
        dp[1] = [triangle[0][0]+triangle[1][0], triangle[0][0]+triangle[1][1]]
        
        for lvl in range(2, len(triangle)):
            dp[lvl] = [0 for _ in range(lvl+1)]
            #print(dp)
            for i in range(lvl+1):
                #print(lvl, i)
                if i > 0 and i <= lvl-1:
                    dp[lvl][i] = min(dp[lvl-1][i-1], dp[lvl-1][i]) + triangle[lvl][i]
                elif i == 0:
                    dp[lvl][i] = dp[lvl-1][i] + triangle[lvl][i]
                else:
                    dp[lvl][i] = dp[lvl-1][i-1] + triangle[lvl][i]

        #print(dp)#
        return min(dp[len(triangle)-1])


# @lc code=end

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
#triangle = [[-10]]

so = Solution()
r = so.minimumTotal(triangle)
print(r)
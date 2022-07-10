#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        dp = cost[0:] + [0]

        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1], dp[i-2]) + dp[i]
            #print(dp)

        return dp[-1]


        
# @lc code=end

if __name__ == "__main__":
    
    cost = [10,15,20]
    cost = [1,100,1,1,1,100,1,1,100,1]

    so = Solution()
    r = so.minCostClimbingStairs(cost)
    print(r)
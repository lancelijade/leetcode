class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        dp = [costs[0]]
        i = 1
        while i < len(costs):
            t = [0] * 3
            for j in range(3):
                t[j] = min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + costs[i][j]
            #print(t)

            dp.append(t)
            i += 1
        
        return min(dp[i-1])




costs = [[17,2,17],[16,16,5],[14,3,19]]
costs = [[7,6,2]]

so = Solution()
r = so.minCost(costs)
print(r)
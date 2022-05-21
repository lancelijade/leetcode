#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from functools import cache
import math


class Solution:

    @cache
    def dp(self, amount: int) -> int:
        if not amount:
            return 0
        if amount in self.coins:
            return 1

        mi = math.inf
        for c in self.coins:
            if amount - c < 0: continue
            r = self.dp(amount - c)
            if r != -1:
                mi = min(mi, r+1)
        return -1 if mi == math.inf else mi


    def coinChange2(self, coins: list[int], amount: int) -> int:
        self.coins = coins
        return self.dp(amount)


    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i-c >= 0:
                    dp[i] = min(dp[i], dp[i-c] + 1)

        return -1 if dp[amount] == math.inf else dp[amount]

        
# @lc code=end

coins = [1,2,5]
amount = 11

"""
coins = [2]
amount = 3

coins = [1]
amount = 0
"""

so = Solution()
r = so.coinChange(coins, amount)
print(r)
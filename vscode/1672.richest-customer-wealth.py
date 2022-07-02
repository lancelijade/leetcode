#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        ma = 0
        for acc in accounts:
            ma = max(ma, sum(acc))
        return ma

        
# @lc code=end

accounts = [[1,2,3],[3,2,1]]
accounts = [[1,5],[7,3],[3,5]]


so = Solution()
r = so.maximumWealth(accounts)
print(r)
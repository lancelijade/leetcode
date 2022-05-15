#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex==0: return [1]
        if rowIndex==1: return [1,1]
        last = self.getRow(rowIndex-1)
        row = [1]
        for i in range(1,rowIndex):
            row.append(last[i-1]+last[i])
        row.append(1)
        return row

        
# @lc code=end

rowIndex = 3

so = Solution()
r = so.getRow(rowIndex)
print(r)
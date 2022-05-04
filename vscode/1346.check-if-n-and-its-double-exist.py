#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        if arr.count(0)>1: return True
        for n in arr:
            if n!=0 and n*2 in arr:
                return True
        return False
        
# @lc code=end

arr = [10,2,5,3]

so = Solution()
r = so.checkIfExist(arr)
print(r)
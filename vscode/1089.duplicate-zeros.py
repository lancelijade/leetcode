#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        le = len(arr)
        i = 0
        while i<le:
            if arr[i] == 0:
                arr.insert(i+1, 0)
                i += 2
                arr.pop()
            else:
                i += 1
        
# @lc code=end

arr = [1,0,2,3,0,4,5,0]

so = Solution()
r = so.duplicateZeros(arr)
print(arr)
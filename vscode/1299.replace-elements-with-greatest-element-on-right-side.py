#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        i = len(arr)-1
        ma = -999999
        while i>=0:
            t = arr[i]
            if ma != arr[i]: arr[i] = ma
            ma = max(ma, t)
            i -= 1
        arr[-1] = -1
        return arr

        
# @lc code=end

arr = [17,18,5,4,6,1]
arr = [400]

so = Solution()
r = so.replaceElements(arr)
print(r)
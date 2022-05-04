#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        le = len(arr)
        if le<3: return False
        top = False
        i = 0
        while i<le-1 and not top:
            if arr[i]==arr[i+1]:
                return False
            elif arr[i]>arr[i+1]:
                if i==0: return False
                top = True
            i += 1

        while i<le-1:
            if arr[i]==arr[i+1]:
                return False
            elif arr[i]<arr[i+1]:
                return False
            i += 1

        return top and True
        
# @lc code=end

arr = [2,1]
arr = [3,5,5]
#arr = [0,3,2,1]
#arr = [0,1,2,3,4,5,6,7,8,9]
arr = [9,8,7,6,5,4,3,2,1,0]

so = Solution()
r = so.validMountainArray(arr)
print(r)
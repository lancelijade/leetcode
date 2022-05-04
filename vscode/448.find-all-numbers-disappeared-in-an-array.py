#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        nn = {x:1 for x in nums}
        r = []
        for i in range(1,len(nums)+1):
            if i not in nn: r.append(i)
        return r
        
# @lc code=end

nums = [4,3,2,7,8,2,3,1]
#nums = [1,1]

so = Solution()
r = so.findDisappearedNumbers(nums)
print(r)
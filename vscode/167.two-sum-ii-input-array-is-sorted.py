#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        a = {}
        for i, n in enumerate(numbers):
            t = target - n
            if t in a and a[t] != i+1:
                return [a[t], i+1]
            a[n] = i+1

        
# @lc code=end

numbers = [2,7,11,15]
target = 9

numbers = [2,3,4]
target = 6

numbers = [-1,0]
target = -1

numbers = [0,0,3,4]
target = 0

so = Solution()
r = so.twoSum(numbers, target)
print(r)
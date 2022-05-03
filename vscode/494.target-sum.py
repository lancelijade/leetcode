#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
from collections import defaultdict
from datetime import datetime 
time_start = datetime.now()

# @lc code=start
class Solution2:

    def dfs(self, pos: int, cursum: int) -> int:
        if pos in self.cache and cursum in self.cache[pos]:
            return self.cache[pos][cursum]

        if pos == self.le-1:
            return (cursum + self.nums[pos] == self.target) + (cursum - self.nums[pos] == self.target)

        r = self.dfs(pos+1, cursum + self.nums[pos]) + self.dfs(pos+1, cursum - self.nums[pos])
        self.cache[pos][cursum] = r
        return r


    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        self.target = target
        self.nums = nums
        self.le = len(nums)
        self.cache = defaultdict(defaultdict)
        return self.dfs(0, 0)


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        le = len(nums)
        i = le-1
        


        
# @lc code=end

nums = [1,1,1,1,1]
target = 3

nums = [1]
target = 1

nums = [42,36,4,15,17,15,31,1,11,2,12,28,22,9,2,31,48,18,48,5]
target = 15

nums = [9,28,50,9,34,48,2,50,38,10,5,16,44,5,48,21,38,17,21,49]
target = 20

so = Solution()
r = so.findTargetSumWays(nums, target)
print(r)


time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)
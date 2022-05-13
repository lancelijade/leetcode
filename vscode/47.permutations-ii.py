#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        n = nums.pop()
        if not nums:
            return [[n]]
        r = set()
        li = self.permuteUnique(nums)
        for t in li:
            for i in range(len(t)+1):
                t1 = list(t)
                t1.insert(i, n)
                r.add(tuple(t1))
        return r

        
# @lc code=end

nums = [1,1,2]
nums = [1,2,3]

so = Solution()
r = so.permuteUnique(nums)
print(r)
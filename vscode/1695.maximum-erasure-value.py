#
# @lc app=leetcode id=1695 lang=python3
#
# [1695] Maximum Erasure Value
#

# @lc code=start
from collections import defaultdict


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        
        d = defaultdict(bool)
        maxscore = 0

        i, j = 0, 0
        score = 0
        
        for j in range(len(nums)):
            if nums[j] not in d:
                score += nums[j]
                maxscore = max(maxscore, score)
                d[nums[j]] = True
            else:
                while i < j:
                    if nums[i] == nums[j]:
                        i += 1
                        break
                    score -= nums[i]
                    del d[nums[i]]
                    i += 1

            #print(i, j, score, maxscore)

        return maxscore

        
# @lc code=end

nums = [4,2,4,5,6]
nums = [5,2,1,2,5,2,1,2,5]

so = Solution()
r = so.maximumUniqueSubarray(nums)
print(r)
#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
import heapq
import math


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        heapq.heapify(nums)

        clen = 0
        lastn = math.inf
        maxlen = 0

        while len(nums) > 0:
            n = heapq.heappop(nums)
            #print(n)

            if n == lastn:
                continue
            elif n == lastn + 1:
                clen += 1
            else:
                clen = 1

            lastn = n
            maxlen = max(maxlen, clen)


        return maxlen


        
# @lc code=end

nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
nums = []

so = Solution()
r = so.longestConsecutive(nums)
print(r)
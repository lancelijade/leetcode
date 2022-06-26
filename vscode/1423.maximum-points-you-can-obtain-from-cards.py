#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#

# @lc code=start
class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        cp = cardPoints * 2
        size = len(cardPoints)
        sm = sum(cp[size-k:size])
        ma = sm
        #print(sm, ma)
        for i in range(size-k+1, size+1):
            #print(i-1, i+k-1)
            sm = sm - cp[i-1] + cp[i+k-1]
            ma = max(ma, sm)
            #print(sm ,ma)
            #if ma == sm: print(cp[i:i+k])

        return ma

        
# @lc code=end

cardPoints = [1,2,3,4,5,6,1]
k = 3
"""

cardPoints = [2,2,2]
k = 2

cardPoints = [9,7,7,9,7,7,9]
k = 7

"""
so = Solution()
r = so.maxScore(cardPoints, k)
print(r)
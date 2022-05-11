#
# @lc app=leetcode id=1641 lang=python3
#
# [1641] Count Sorted Vowel Strings
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n==1: return 5

        d = [[0,0,0,0,0] for _ in range(n)]
        #print(d)
        d[0] = [1,1,1,1,1]
        for i in range(1, n):
            for j in range(0,5):
                for k in range(0,j+1):
                    d[i][j] += d[i-1][k]
        #print(d)
        return sum(d[n-1])

        
# @lc code=end

n = 33

so = Solution()
r = so.countVowelStrings(n)
print(r)
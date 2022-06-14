#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#

# @lc code=start
from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @cache
        def lcs(w1: str, w2: str, i: int, j: int) -> int:
            if not i or not j:
                return 0

            if w1[i-1] == w2[j-1]:
                return lcs(w1, w2, i-1, j-1) + 1

            return max(lcs(w1, w2, i-1, j), lcs(w1, w2, i, j-1))


        m = len(word1)
        n = len(word2)
        return m + n - 2 * lcs(word1, word2, m, n)
        

        
# @lc code=end

word1 = "seea"
word2 = "eat"

word1 = "leetcode"
word2 = "etco"

word1 = "sea"
word2 = "ate"

word1 = "teacher"
word2 = "teared"

so = Solution()
r = so.minDistance(word1, word2)
print(r)
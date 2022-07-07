#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @cache
        def dp(i, p1, p2):
            if i >= size: return True

            if p1 < size1 and s3[i] == s1[p1]:
                r = dp(i+1, p1+1, p2)
                if r: return True

            if p2 < size2 and s3[i] == s2[p2]:
                r = dp(i+1, p1, p2+1)
                if r: return True

            return False


        size = len(s3)
        size1 = len(s1)
        size2 = len(s2)

        if size != size1 + size2: return False

        return dp(0, 0, 0)

        
# @lc code=end


if __name__ == "__main__":

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"

    s1 = ""
    s2 = ""
    s3 = ""

    so = Solution()
    r = so.isInterleave(s1, s2, s3)
    print(r)
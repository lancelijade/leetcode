#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
from functools import cache


class Solution:
    @cache
    def isPalindromic(self, s: str, p: int, q: int) -> bool:
        #print("isParlindromic:", p, q)
        if p >= q: return True
        if p < q: 
            if s[p] != s[q]: 
                return False
            else:
                return self.isPalindromic(s, p+1, q-1)


    def countSubstrings(self, s: str) -> int:
        r = len(s)
        for le in range(2, len(s)+1):
            for i in range(len(s)-le+1):
                #print("le, i:", le, i)
                if self.isPalindromic(s, i, i+le-1):
                    r += 1
        return r
        
# @lc code=end

s = "abc"
so = Solution()
r = so.countSubstrings(s)
print(r)
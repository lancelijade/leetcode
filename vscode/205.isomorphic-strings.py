#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        size = len(s)
        d = defaultdict(str)

        for i in range(size):
            if s[i] not in d:
                if t[i] not in d.values():
                    d[s[i]] = t[i]
                else:
                    return False
            else:
                if d[s[i]] != t[i] and d[t[i]] != s[i]:
                    return False
            #print(d)

        return True


        
# @lc code=end

s = "paper"
t = "title"

s = "egg"
t = "add"

s = "foo"
t = "bar"


s = "badc"
t = "baba"
"""
"""
so = Solution()
r = so.isIsomorphic(s, t)
print(r)
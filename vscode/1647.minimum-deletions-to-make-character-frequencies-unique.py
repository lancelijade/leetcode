#
# @lc app=leetcode id=1647 lang=python3
#
# [1647] Minimum Deletions to Make Character Frequencies Unique
#

# @lc code=start
from typing import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        li = Counter(s)
        #print(li)
        va = {}
        r = 0
        for k, v in li.items():
            if v not in va:
                va[v] = k
            else:
                while v>=1:
                    v -= 1
                    r += 1
                    if not v: break
                    if v not in va:
                        va[v] = k
                        break

        #print(va)
        return r
        
# @lc code=end

s = "aaabbbcc"
#s = "ceabaacb"
#s = "aab"

so = Solution()
r = so.minDeletions(s)
print(r)
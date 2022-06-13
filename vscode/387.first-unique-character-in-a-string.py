#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
import math
from typing import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, c in enumerate(s):
            if c in d:
                d[c] = math.inf
            else:
                d[c] = i
        
        r = sorted(d.values())[0] 
        return r if r != math.inf else -1

        
# @lc code=end

s = "leetcode"
s = "loveleetcode"
s = "aabb"

so = Solution()
r = so.firstUniqChar(s)
print(r)
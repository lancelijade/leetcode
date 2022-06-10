#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        clen = 0
        mlen = 0
        for n, c in enumerate(s):
            if c not in d or d[c] is None:
                d[c] = n
                clen += 1
            else:
                clen = n - d[c]
                for k, v in d.items():
                    if v is None:
                        continue
                    if v < d[c]:
                        d[k] = None
                d[c] = n
            #print(c, clen, mlen, d)
            mlen = max(mlen, clen)
        return mlen

        
# @lc code=end

s = "pwwkew"
s = "abcabcbb"
#s = "bbbbb"
#s = "dvdf"
#s = "abba"

so = Solution()
r = so.lengthOfLongestSubstring(s)
print(r)
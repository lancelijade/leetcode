#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
from collections import defaultdict


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        r = {}
        q = []
        ma = 0

        for ce, c in enumerate(s):
            if c == '(':
                q.append(ce)

            else:
                if not q: continue
                cs = q.pop()
                rec = False
                for bs, be in r.items():
                    if cs - bs == 1 or cs == be + 1:
                        r[bs] = ce
                        ma = max(ma, ce-bs+1)
                        rec = True
                        break
                if not rec:
                    r[cs] = ce
                    ma = max(ma, ce-cs+1)

        return ma

        
# @lc code=end

s = ")()())"
#s = "(()"
s = ""
s = "()(()"

so = Solution()
r = so.longestValidParentheses(s)
print(r)
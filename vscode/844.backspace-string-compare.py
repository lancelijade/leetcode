#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:

    def typing(self, s: str) -> str:
        i, j = 0, 0
        s = list(s)
        while j<len(s):
            s[i] = s[j]
            if s[j]=='#':
                i -= 1
                if i<0: i=0
                j += 1
            else:
                i += 1
                j += 1
                
        return s[:i]

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.typing(s) == self.typing(t)
        
# @lc code=end


s = "ab#c"
t = "ad#c"

s = "ab##"
t = "c#d#"

s = "a#c"
t = "b"

so = Solution()
r = so.backspaceCompare(s, t)
print(r)
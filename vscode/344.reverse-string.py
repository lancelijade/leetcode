#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: list[str], start=0, end=None) -> None:
        if end is None: end = len(s)-1
        if end-start>=1:
            s[start], s[end] = s[end], s[start]
            self.reverseString(s, start+1, end-1)
        
# @lc code=end

s = ["h","e","l","l","o"]
#s = ["H","a","n","n","a","h"]
s = [1,2,3,4,5,6]

so = Solution()
r = so.reverseString(s)
print(s)
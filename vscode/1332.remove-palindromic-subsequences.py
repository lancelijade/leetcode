#
# @lc app=leetcode id=1332 lang=python3
#
# [1332] Remove Palindromic Subsequences
#

# @lc code=start
class Solution:
    def removePalindromeSub(self, s: str) -> int:

        if s.find('a') != -1 and s.find('b') != -1:
            if s == s[::-1]:
                return 1
            return 2
        else:
            return 1

        
# @lc code=end

s = "1baabb1baabb"
s = "ababa"
#s = "bbaabaaa"

so = Solution()
r = so.removePalindromeSub(s)
print(r)
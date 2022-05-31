#
# @lc app=leetcode id=1461 lang=python3
#
# [1461] Check If a String Contains All Binary Codes of Size K
#

# @lc code=start
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        t = set()
        for i in range(len(s)-k+1):
            t.add(s[i:i+k])
        print(t)
        return len(t) == 2 ** k

        
# @lc code=end

s = "00110110"
k = 3

so = Solution()
r = so.hasAllCodes(s, k)
print(r)
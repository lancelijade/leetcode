#
# @lc app=leetcode id=1461 lang=python3
#
# [1461] Check If a String Contains All Binary Codes of Size K
#

# @lc code=start
class Solution:
    def hasAllCodes2(self, s: str, k: int) -> bool:
        a = [0] * 2 ** k
        for i in range(len(s)-k+1):
            n = int(s[i:i+k], 2)
            a[n] = 1
        #print(a)
        return sum(a) == 2**k


    def hasAllCodes(self, s: str, k: int) -> bool:
        t = set()
        for i in range(len(s)-k+1):
            t.add(s[i:i+k])
        #print(t)
        return len(t) == 2 ** k


        
# @lc code=end

s = "0110"
k = 2

so = Solution()
r = so.hasAllCodes(s, k)
print(r)
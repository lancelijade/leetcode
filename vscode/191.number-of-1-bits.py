#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        r = 0
        while 1:
            if n & 1:
                r += 1

            n >>= 1
            if not n:
                break

        return r

        
# @lc code=end

n = 0b00000000000000000000000000001011
n = 0b00000000000000000000000010000000

so = Solution()
r = so.hammingWeight(n)
print(r)
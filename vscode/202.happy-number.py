#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:

    def __init__(self) -> None:
        self.r = set()

    def isHappy(self, n: int) -> bool:
        
        su = 0
        while n>0:
            n, m = divmod(n, 10)
            su += m * m
        
        if su == 1:
            return True
        elif su in self.r:
            return False
        else:
            self.r.add(su)
            return self.isHappy(su)

        
# @lc code=end

n = 2

so = Solution()
r = so.isHappy(n)
print(r)
#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start
from typing import Counter


class Solution:

    # simulate
    def numberOfSteps2(self, num: int) -> int:
        r = 0
        while num != 0:
            num = num / 2 if num % 2 == 0 else num - 1
            r += 1
        return r
        

    # bit op
    def numberOfSteps(self, num: int) -> int:
        r = 0
        while num > 1:
            if num & 1:
                r += 2
            else:
                r += 1
            num >>= 1
        return r + 1 if num == 1 else r


    # string count
    def numberOfSteps4(self, num: int) -> int:
        bi = bin(num)
        return Counter(bi)['1'] + len(bi) - 3


# @lc code=end

num = 123

so = Solution()
r = so.numberOfSteps(num)
print(r)
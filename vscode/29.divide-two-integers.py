#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
from typing import OrderedDict


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend < divisor: return 0

        map = OrderedDict()
        sumd = divisor
        n = 1
        while sumd <= dividend:
            map[sumd] = n
            sumd += sumd
            n += n
        #print(map)

        sumd = 0
        r = 0
        while dividend > sumd:
            if dividend - sumd < divisor: break

            for k, v in reversed(map.items()):
                if sumd + k <= dividend:
                    sumd += k
                    r += v
                    break

        r = sign * r
        if r > 2147483647: return 2147483647
        elif r < -2147483648: return -2147483648
        else: return r


        
# @lc code=end

dividend = 10
divisor = 3

dividend = 7
divisor = -3

dividend = 1
divisor = 1

so = Solution()
r = so.divide(dividend, divisor)
print(r)
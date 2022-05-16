#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
from sortedcontainers import SortedDict


class Solution:
    def myPow(self, x: float, n: int) -> float:

        cache = SortedDict({1: x})

        def helper(x: float, n: int, cur: float, curn: int) -> float:
            #print(x, n, cur, curn)
            if cur==0 or n==0: return cur
            if n>curn:
                cache[curn*2] = cur*cur
                return helper(x, n-curn, cur*cur, curn*2)
            else:
                for k, v in reversed(cache.items()):
                    #print('incache:', k, v)
                    if n>=k:
                        cache[curn-k] = cur*v
                        return helper(x, n-k, cur*v, curn-k)

        if n==0:
            return 1
        elif n>0:
            return helper(x, n-1, x, 1)
        else:
            r = helper(x, -n-1, x, 1)
            if r: return 1/r
            else: return 0

        
# @lc code=end

def log(func):
    def wrapper(*args, **kw):
        from datetime import datetime 
        time_start = datetime.now()
        #print('call %s():' % func.__name__)
        r = func(*args, **kw)
        time_end = datetime.now()
        print("---\ntime cost:",time_end-time_start)
        return r
    return wrapper

@log
def run(*args, **kw):
    so = Solution()
    r = so.myPow(*args, **kw)
    print(r)

x = 2.00000
n = 10

x = 2.10000
n = 3

x = 2.00000
n = -2


x = 0.00001
n = 2147483647

x = -2.00000
n = 2

x = 0.22838
n = 7


x = 0.99999
n = 948688
"""
"""
run(x, n)

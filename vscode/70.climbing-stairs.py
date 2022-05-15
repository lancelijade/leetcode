#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
from functools import cache

class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        return n if n <=2 else self.climbStairs(n-2)+self.climbStairs(n-1)
        
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
def run(x):
    so = Solution()
    r = so.climbStairs(x)
    print(r)

n = 20
run(n)
#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
from functools import cache

class Solution:
    @cache
    def fib(self, n: int) -> int:
        return n if n < 2 else self.fib(n-2) + self.fib(n-1)
        
        
# @lc code=end

n = 42


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
def run():
    so = Solution()
    r = so.fib(n)
    print(r)

run()
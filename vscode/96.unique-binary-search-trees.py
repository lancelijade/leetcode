#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
from functools import cache


class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n==0 or n==1: return 1
        r = 0
        for i in range(1, n+1):
            r += self.numTrees(i-1) * self.numTrees(n-i)
        return r
        
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
    r = so.numTrees(*args, **kw)
    print(r)

n = 19
run(n)
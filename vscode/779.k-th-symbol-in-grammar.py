#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        #print(n, k)
        if n == 1: return 0
        if k <= pow(2, n-2): 
            return self.kthGrammar(n-1, k)
        else:
            return (self.kthGrammar(n-1, k-pow(2, n-2)) + 1) % 2

        
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
    r = so.kthGrammar(*args, **kw)
    print(r)

n = 3
k = 2

run(n, k)

"""
0
01
0110
01101001
0110100110010110
"""
#
# @lc app=leetcode id=1354 lang=python3
#
# [1354] Construct Target Array With Multiple Sums
#

# @lc code=start
class Solution:

    def isPossible(self, target: list[int]) -> bool:

        if target == [1]: return True
        size = len(target)
        if size == 1: return False

        su = sum(target)

        while 1:
            #print(target)

            ma = max(target)
            other = su - ma
            if other == 1:
                return True

            n = ma % other
            if n == ma or n == 0: 
                return False

            target[target.index(ma)] = n
            su -= ma - n
            
            if sum(target) == size: return True


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
    r = so.isPossible(*args, **kw)
    print(r)

target = [9,3,5]
#target = [1,1,1,2]
#target = [8,5]
#target = [1,1000000000]
#target = [1]

run(target)
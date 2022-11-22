#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
from collections import defaultdict, deque
import pprint
pp = pprint.PrettyPrinter()
from datetime import datetime 
time_start = datetime.now()

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        ns = []
        for i in range(int(n**0.5), 0, -1):
            ns.append(i*i)
        #print(ns)

        q = deque()
        for i in ns:
            if i==n: return 1
            elif i<n: q.append((i, i, 1))
        #print(q)

        while q:
            cur_sum, cur, cnt = q.popleft()

            for i in ns:
                if i<=cur and cur_sum+i<=n:
                    if cur_sum+i == n: return cnt+1
                    q.append((cur_sum+i, i, cnt+1))

        
# @lc code=end

n = 9999

so = Solution()
r = so.numSquares(n)
print(r)

time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)
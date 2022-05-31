#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
from collections import deque


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        q = deque()
        q.extend([x] for x in range(1, n+1))
        #print(q)

        while len(q[0]) < k:
            x = q.popleft()
            for i in range(x[-1]+1, n+1):
                q.append(x + [i])

        return q
        
# @lc code=end

n = 4
k = 3

so = Solution()
r = so.combine(n, k)
print(r)
#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
from collections import defaultdict


class Solution:

    def re(self, k, n, path):
        if path is None:
            path = []

        #print(k, n, path)
        if k==1:
            if 1<=n<=9 and n>path[-1]:
                path.append(n)
                self.r.append(path)
            return 

        if path: rn = path[-1]+1
        else: rn = 1

        for i in range(rn, 10):
            if i in path: continue
            if n-i<0: break
            self.re(k-1, n-i, path+[i])



    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        
        if n<(1+k)*k/2 or n>45: return []

        self.r = []
        self.re(k, n, [])
        return self.r


        
# @lc code=end

k = 3
n = 9

so = Solution()
r = so.combinationSum3(k, n)
print(r)
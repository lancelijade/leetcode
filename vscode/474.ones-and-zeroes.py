#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#
from pprint import pprint

# @lc code=start
from typing import Counter


class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        na = {}
        c = Counter(strs[0])
        na[-1] = {(0, 0): 0}
        
        for i in range(len(strs)):
            c = Counter(strs[i])
            na[i] = {}

            for k, v in na[i-1].items():
                if k in na[i]:
                    na[i][k] = max(v, na[i][k])
                else:
                    na[i][k] = v

                if k[0]+c['0']>m or k[1]+c['1']>n: continue

                key = (k[0]+c['0'], k[1]+c['1'])
                
                if key in na[i]:
                    na[i][key] = max(na[i][key], v+1)
                else:
                    na[i][key] = v + 1

        #pprint(na)
        return max(na[i].values())

        
# @lc code=end

strs = ["10","0001","111001","1","0"]
m = 5
n = 3

strs = ["10","0","1"]
m = 1
n = 1

strs = ["10","0001","111001","1","0"]
m = 3
n = 4

strs = ["10","0","1"]
m = 1
n = 1

strs = ["00","000"]
m = 1
n = 10

so = Solution()
r = so.findMaxForm(strs, m, n)
print(r)
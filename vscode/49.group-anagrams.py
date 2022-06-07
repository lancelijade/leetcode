#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list[str])
        for s in strs:
            t = list(s)
            t.sort()
            t = tuple(t)
            d[t].append(s)
        #print(d)
        return d.values()

        
# @lc code=end

strs = ["eat","tea","tan","ate","nat","bat"]

so = Solution()
r = so.groupAnagrams(strs)
print(r)
#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
from typing import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = Counter(list(stones))
        r = 0
        for c in jewels:
            r += cnt[c]
        return r

        
# @lc code=end

jewels = "aA"
stones = "aAAbbbb"

jewels = "z"
stones = "ZZ"

so = Solution()
r = so.numJewelsInStones(jewels, stones)
print(r)
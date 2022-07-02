#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
from typing import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = Counter(ransomNote)
        d2 = Counter(magazine)

        for d, v in d1.items():
            if d not in d2 or d2[d] < v:
                return False

        return True

        
# @lc code=end

ransomNote = "aa"
magazine = "aab"

ransomNote = "a"
magazine = "b"

ransomNote = "aa"
magazine = "ab"


so = Solution()
r = so.canConstruct(ransomNote, magazine)
print(r)
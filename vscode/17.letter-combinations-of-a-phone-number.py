#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits: return []

        r = ['']
        map = [ None, None, 
                ['a', 'b', 'c'],
                ['d', 'e', 'f'],
                ['g', 'h', 'i'],
                ['j', 'k', 'l'],
                ['m', 'n', 'o'],
                ['p', 'q', 'r', 's'],
                ['t', 'u', 'v'],
                ['w', 'x', 'y', 'z']
                ]
        di = list(digits)
        
        i = 0
        while i < len(di):
            d = int(di[i])
            r2 = []
            for ch in map[d]:
                for s1 in r:
                    r2.append(s1+ch)
            r = r2
            i += 1

        return r

        
# @lc code=end

digits = "23"
digits = ""
digits = "2349"

so = Solution()
r = so.letterCombinations(digits)
print(r)
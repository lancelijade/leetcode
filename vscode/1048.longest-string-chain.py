#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#

# @lc code=start
from functools import cache


class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        
        @cache
        def dfs(word: str) -> list[str]:
            if len(word) == 1:
                return [word]

            maxlen = 1
            r = [word]

            for i in range(len(word)):
                if i == 0:
                    w = word[1:]
                elif i == len(word) -1:
                    w = word[:-1]
                else:
                    w = word[:i] + word[i+1:]
                
                if w in wds:
                    r1 = dfs(w) + [word]
                    if len(r1) > maxlen:
                        r = r1
                        maxlen = len(r1)

            return r


        wds = set(words)
        maxlen = 0

        for word in wds:
            lst = dfs(word)
            #print(word, lst)
            size = len(lst)
            if size > maxlen:
                maxlen = size

        return maxlen

        
# @lc code=end

words = ["a","b","ba","bca","bda","bdca"]
words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
words = ["abcd","dbqca"]
words = ["a","ab","ac","bd","abc","abd","abdd"]


so = Solution()
r = so.longestStrChain(words)
print(r)
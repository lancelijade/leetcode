#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start

class Solution:
    def maxProduct(self, words: list[str]) -> int:
        d = []
        for word in words:
            d.append([set(word), len(word)])
        #print(d)

        ma = 0
        for i in range(len(d)):
            for j in range(i+1, len(d)):
                if not d[i][0].intersection(d[j][0]):
                    ma = max(ma, d[i][1] * d[j][1])
        return ma


        
# @lc code=end

words = ["abcw","baz","foo","bar","xtfn","abcdef"]
words = ["a","ab","abc","d","cd","bcd","abcd"]
words = ["a","aa","aaa","aaaa"]

so = Solution()
r = so.maxProduct(words)
print(r)
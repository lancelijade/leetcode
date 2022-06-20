#
# @lc app=leetcode id=820 lang=python3
#
# [820] Short Encoding of Words
#

# @lc code=start
class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        #wd = {}
        #for i, word in enumerate(words):
        #    wd[word] = i

        indices = [-1] * len(words)
        #print(wd, indices)

        ws = sorted(words, key=len, reverse=True)
        r = ''
        for w in ws:
            pos = r.find(w + '#')
            if pos != -1:
                1
                #indices[wd[w]] = pos
            else:
                pos = len(r)
                #indices[wd[w]] = pos
                r += w + '#'

        #print(indices)
        return len(r)



        
# @lc code=end

words = ["time", "me", "bell"]
#words = ["t"]

so = Solution()
r = so.minimumLengthEncoding(words)
print(r)
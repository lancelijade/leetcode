#
# @lc app=leetcode id=820 lang=python3
#
# [820] Short Encoding of Words
#

# @lc code=start
from collections import defaultdict
from functools import reduce


class Solution:
    def minimumLengthEncoding2(self, words: list[str]) -> int:

        ws = sorted(words, key=len, reverse=True)
        r = ''
        for w in ws:
            pos = r.find(w + '#')
            if pos == -1:
                r += w + '#'

        #print(indices)
        return len(r)


    def minimumLengthEncoding(self, words):
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)


        
# @lc code=end

words = ["time", "me", "bell"]
#words = ["t"]

so = Solution()
r = so.minimumLengthEncoding(words)
print(r)
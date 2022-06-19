#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start
from collections import defaultdict
Trie = lambda: defaultdict(Trie)

class Solution:

    def __init__(self):
        self.trie = Trie()


    def addWord(self, word: str) -> None:
        cur = self.trie
        for ch in word:
            cur = cur[ch]
        cur['$'] = True


    def preorder(self, tr: Trie) -> list[str]:
        
        r = []
        for ch in sorted(tr.keys()):
            if len(r) > 3: break
            if ch == '$':
                r.append('')
            else:
                li = self.preorder(tr[ch])
                for s in li:
                    r.append(ch + s)
                    if len(r) > 3: break

        return r


    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        for p in products:
            self.addWord(p)

        cur = self.trie
        r = []
        for i, ch in enumerate(searchWord):
            rc = []
            li = self.preorder(cur[ch])[:3]
            for s in li:
                rc.append(searchWord[:i+1]+s)
            r.append(rc)
            cur = cur[ch]

        return r

        

        
# @lc code=end

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

"""
products = ["havana"]
searchWord = "havana"

products = ["bags","baggage","banner","box","cloths"]
searchWord = "bags"
"""

so = Solution()
r = so.suggestedProducts(products, searchWord)
print(r)
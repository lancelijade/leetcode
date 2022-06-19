#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
from collections import defaultdict
Trie = lambda: defaultdict(Trie)

class WordDictionary:

    def __init__(self):
        self.trie = Trie()


    def addWord(self, word: str) -> None:
        cur = self.trie
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['$'] = True
        #print(self.trie)


    def search(self, word: str, cur=None) -> bool:
        if not cur:
            cur = self.trie

        if not word:
            if '$' in cur:
                return True
            else:
                return False

        ch = word[0]
        if ch == '.':
            r = False
            for cu in cur.keys():
                if cu != '$':
                    r |= self.search(word[1:], cur[cu])
                    if r: return r
            return r

        if ch not in cur:
            return False
        
        return self.search(word[1:], cur[ch])


# @lc code=end

in1 = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
in2 = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

in1 = ["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
in2 = [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]

in1 = ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
in2 = [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
#[null,null,null,null,null,false,false,null,true,true,false,false,true,false]

o = None
cmd = []
ret = []
if in2[0]:
    cmd.append('o = {}({})'.format(in1[0], in2[0][0]))
else:
    cmd.append('o = {}()'.format(in1[0]))

for i in range(1, len(in1)):
    if (len(in2[i])>0):
        cmd.append('ret.append(o.{}("{}"))'.format(in1[i], in2[i][0]))
    else:
        cmd.append('ret.append(o.{}())'.format(in1[i]))

for cmdd in cmd:
    print(cmdd)
    exec(cmdd)

print(ret)
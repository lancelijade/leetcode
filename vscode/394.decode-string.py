#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
from var_dump import var_dump

# @lc code=start
import string

class Node:
    def __init__(self, val=None, children=[], pos=-1):
        self.val = val
        self.pos = pos
        self.children = children


class Solution:
    def build(self, s: str) -> Node:
        head = Node(1, [], -1)
        n = 0
        i = 0
        while i<len(s):
            c = s[i]
            if c in string.ascii_lowercase:
                x = Node(c, [], i)
                head.children.append(x)
                i += 1
            elif c in string.digits:
                n = n*10 + int(c)
                i += 1
            elif c == '[':
                r = self.build(s[i+1:])
                r.val = n
                head.children.append(r)
                i += r.pos + 1
                n = 0
            elif c == ']':
                head.pos = i+1
                return head
        return head


    def lvlord(self, root: Node) -> str:
        s = ''
        for nd in root.children:
            if str(nd.val) in string.ascii_lowercase:
                s += nd.val
            else:
                s += self.lvlord(nd)
        return s * root.val


    def decodeString(self, s: str) -> str:
        t = self.build(s)
        return self.lvlord(t)

        
# @lc code=end

s = "3[a2[c]]"
s = "3[a]2[bc]"
s = "2[abc]3[cd]ef"

so = Solution()
r = so.decodeString(s)
print(r)
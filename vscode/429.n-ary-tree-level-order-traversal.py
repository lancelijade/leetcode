#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#

import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump
from collections import deque

# @lc code=start
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: Node) -> list[list[int]]:

        if not root: return []

        q = deque()
        q.append(root)
        r = [[root.val]]

        while q:
            lvl = []
            for _ in range(len(q)):
                node = q.popleft()
                for child in node.children:
                    lvl.append(child.val)
                    q.append(child)

            r.append(lvl)

        return r[:-1]

        
# @lc code=end


def TreeBuild(root: list[int]) -> Node:

    if not root: return None

    head = Node(-1)
    h = head
    q = deque()
    g = []

    for va in root:
        if not va:
            h.children = g
            g = []
            h = q.popleft()
            continue
        
        node = Node(va)
        g.append(node)
        q.append(node)

    if q:
        h.children = g

    return head.children[0]


root = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
root = [1,None,3,2,4,None,5,6]

tree = TreeBuild(root)
#var_dump(tree)
so = Solution()
r = so.levelOrder(tree)
pp.pprint(r)
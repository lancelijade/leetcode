#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump
from collections import deque

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:

        if not root: return root

        q = deque()
        lvl = 0
        q.append([root,lvl])
        h = Node(-1)
        last = h
        
        while q:
            #var_dump(q)
            node, lvln = q.popleft()
            if lvln == lvl: 
                last.next = node
            else:
                lvl = lvln
            last = node

            if node.left: q.append([node.left, lvl+1])
            if node.right: q.append([node.right, lvl+1])

        return h.next

        
# @lc code=end


def treeBuild(root: list[int]) -> Node:
    
    if not root: return root
    
    le = len(root)

    a = []
    for val in root:
        node = Node(val)
        a.append(node)
    #var_dump(a)

    for i, node in enumerate(a):
        if i*2+1 < le: node.left = a[i*2+1]
        if i*2+2 < le: node.right = a[i*2+2]

    return a[0]

root = [1,2,3,4,5,6,7]
root = []

tree = treeBuild(root)
#var_dump(tree)
so = Solution()
r = so.connect(tree)
var_dump(r)
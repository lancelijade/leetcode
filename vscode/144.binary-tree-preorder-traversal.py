#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump
from collections import defaultdict
import math
import heapq
from collections import deque
from datetime import datetime 
time_start = datetime.now()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hardBSTreeBuild(root: list[int]) -> TreeNode:
    
    if not root: return None

    le = len(root)

    a = []
    for val in root:
        if val is None: node = None
        else: node = TreeNode(val)
        a.append(node)

    i = 0
    j = 1
    while j < le:
        if a[i]:
            if a[j]: 
                a[i].left = a[j]
            j += 1

            if j == le: break
            
            if a[j]:
                a[i].right = a[j]
            j += 1
        i += 1
    return a[0]


# @lc code=start

class Solution:

    def preorder(self, root: TreeNode) -> list[int]:
        if not root: return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

    def preorderIter(self, root: TreeNode) -> list[int]:
        if not root: return []

        out = []
        q = deque()
        q.append(root)

        while q:
            node = q.pop()
            out.append(node.val)
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)

        return out


    def preorderTraversal(self, root: TreeNode) -> list[int]:
        return self.preorderIter(root)

        
# @lc code=end

root = [1,None,2,3]
#root = []
#root = [1]
#root = [3,1,2]
#root = [1,4,3,2]



tree = hardBSTreeBuild(root)
so = Solution()
r = so.preorderTraversal(tree)
print(r)


time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)
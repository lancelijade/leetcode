#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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

    def levelOrderIter(self, root: TreeNode) -> list[list[int]]:
        if not root: return []
        
        lvl = 0
        q = deque()
        q.append((root, lvl))
        r = []

        while q:
            node, lvl = q.popleft()
            if len(r)-1<lvl:
                r.append([])
            r[lvl].append(node.val)
            if node.left: q.append((node.left, lvl+1))
            if node.right: q.append((node.right, lvl+1))

        return r

    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        return self.levelOrderIter(root)
        
# @lc code=end


root = [3,9,20,None,None,15,7]
#root = [1]
#root = []


tree = hardBSTreeBuild(root)
so = Solution()
r = so.levelOrder(tree)
print(r)


time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)
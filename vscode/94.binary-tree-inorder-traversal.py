#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
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

    def inorder(self, root: TreeNode) -> list[int]:
        if not root: return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def inorderIter(self, root: TreeNode) -> list[int]:
        if not root: return []

        out = []
        q = deque()
        curr = root

        while curr or q:
            while curr:
                q.append(curr)
                curr = curr.left
            curr = q.pop()
            out.append(curr.val)
            curr = curr.right

        return out


    def inorderTraversal(self, root: TreeNode) -> list[int]:
        return self.inorderIter(root)



# @lc code=end

root = [1,None,2,3]
root = [3,1,2]
root = [1,4,3,2]


tree = hardBSTreeBuild(root)
so = Solution()
r = so.inorderTraversal(tree)
print(r)


time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)
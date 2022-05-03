#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
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

    def postorder(self, root: TreeNode) -> list[int]:
        if not root: return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.val]

    def postorderIter(self, root: TreeNode) -> list[int]:
        if not root: return []

        res = []
        stack = deque()
        node = root
        last_visited_node = None

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            # no right subtree, right subtree was visited
            if stack[-1].right in [None, last_visited_node]:
                res.append(stack[-1].val)
                last_visited_node = stack.pop()
                
            # right subtree was not visited
            else:
                node = stack[-1].right

        return res

    def postorderTraversal(self, root: TreeNode) -> list[int]:
        return self.postorderIter(root)
        

# @lc code=end


root = [1,None,2,3]
#root = []
#root = [1]
root = [3,1,2]
#root = [1,4,3,2]


tree = hardBSTreeBuild(root)
so = Solution()
r = so.postorderTraversal(tree)
print(r)


time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)
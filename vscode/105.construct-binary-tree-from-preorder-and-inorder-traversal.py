#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
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

# @lc code=start
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:

        if not preorder: return None
        head = TreeNode(preorder[0])

        left_len = inorder.index(head.val)

        head.left = self.buildTree(preorder[1:left_len+1], inorder[:left_len])
        head.right = self.buildTree(preorder[left_len+1:], inorder[left_len+1:])

        return head
        
# @lc code=end

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]


so = Solution()
r = so.buildTree(preorder, inorder)
var_dump(r)

time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)
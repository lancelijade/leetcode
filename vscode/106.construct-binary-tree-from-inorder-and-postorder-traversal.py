#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
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
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:

        if not inorder: return None

        head = TreeNode(postorder[-1])

        len_left = inorder.index(head.val)

        head.left = self.buildTree(inorder[:len_left], postorder[:len_left])
        head.right = self.buildTree(inorder[len_left+1:], postorder[len_left:-1])
        #var_dump(head)

        return head

        
# @lc code=end


inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

so = Solution()
r = so.buildTree(inorder, postorder)
var_dump(r)

time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)
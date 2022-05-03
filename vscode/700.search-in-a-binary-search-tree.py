#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeBuild(root: list[int]) -> TreeNode:

    le = len(root)

    a = []
    for val in root:
        node = TreeNode(val)
        a.append(node)
    #var_dump(a)

    for i, node in enumerate(a):
        if i*2+1 < le: node.left = a[i*2+1]
        if i*2+2 < le: node.right = a[i*2+2]

    return a[0]


# @lc code=start
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if not root or not root.val:
            return None
        
        elif val == root.val:
            return root

        elif val < root.val:
            return self.searchBST(root.left, val)

        else:
            return self.searchBST(root.right, val)
        

# @lc code=end


root = [4,2,7,1,3]
val = 2

node = treeBuild(root)
so = Solution()
r = so.searchBST(node, val)
var_dump(r)
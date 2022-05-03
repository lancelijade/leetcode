#
# @lc app=leetcode id=669 lang=python3
#
# [669] Trim a Binary Search Tree
#

import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:

        def trim(node):
            if not node:
                return None
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)

        
# @lc code=end

def BSTTreeBuild(root: list[int]) -> TreeNode:
    
    le = len(root)

    a = []
    for val in root:
        if val is None: 
            node = None
        else: 
            node = TreeNode(val)
        a.append(node)
    #var_dump(a)

    h = a[0]
    i = 1
    while i < le:
        if not a[i]:
            i += 1
            continue

        if a[i].val < h.val:
            if not h.left:
                h.left = a[i]
            else:
                h = h.left
                continue
        else:
            if not h.right:
                h.right = a[i]
            else:
                h = h.right
                continue

        h = a[0]
        i += 1

    return a[0]


root = [1,0,2]
low = 1
high = 2

root = [3,0,4,None,2,None,None,1]
low = 1
high = 3

tree = BSTTreeBuild(root)
#var_dump(tree)
so = Solution()
r = so.trimBST(tree, low, high)
var_dump(r)
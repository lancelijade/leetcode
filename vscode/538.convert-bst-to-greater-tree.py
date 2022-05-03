#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def BSTreeBuild(root: list[int]) -> TreeNode:
    
    if not root: return None

    le = len(root)

    a = []
    for val in root:
        if val is None: node = None
        else: node = TreeNode(val)
        a.append(node)

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


# @lc code=start

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        if not root: return None

        def radd(root, rsum):

            if root.right:
                root.val += radd(root.right, rsum)
            else:
                root.val += rsum

            if root.left:
                return radd(root.left, root.val)
            else:
                return root.val

        radd(root, 0)
        return root
        
# @lc code=end


root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
root = [0,None,1]
root = []

tree = BSTreeBuild(root)
#var_dump(tree)
so = Solution()
r = so.convertBST(tree)
var_dump(r)
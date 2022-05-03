#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
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

    def __init__(self) -> None:
        self.arr = []

    def lnr(self, root: TreeNode):
        if root.left: self.increasingBST(root.left)
        self.arr.append(root)
        if root.right: self.increasingBST(root.right)


    def increasingBST(self, root: TreeNode) -> TreeNode:

        self.lnr(root)
        n = len(self.arr)
        head = TreeNode(-1)
        h = head

        for node in self.arr:
            h.right = node
            h = h.right
            h.left = None

        return head.right


# @lc code=end

root = [5,3,6,2,4,None,8,1,None,None,None,7,9]
root = [5,1,7]

tree = BSTreeBuild(root)
#var_dump(tree)
so = Solution()
r = so.increasingBST(tree)
var_dump(r)
#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump

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
    def __init__(self):
        self.a = []

    def lnr(self, node: TreeNode):
        if node.left: self.lnr(node.left)
        self.a.append(node)
        if node.right: self.lnr(node.right)

    def recoverTree(self, root: TreeNode) -> None:
        self.lnr(root)

        err = []
        for i in range(1, len(self.a)):
            #print(start, i)
            if self.a[i].val < self.a[i-1].val:
                err.append((i-1, i))
            if len(err) == 2:
                self.swap(err[0][0], err[1][1])
                return

        self.swap(err[0][0], err[0][1])


    def swap(self, n1, n2):
        self.a[n1].val, self.a[n2].val = self.a[n2].val, self.a[n1].val

        
# @lc code=end

root = [1,3,None,None,2]
root = [3,1,4,None,None,2]
root = [146,71,-13,55,None,231,399,321,None,None,None,None,None,-33]


tree = hardBSTreeBuild(root)
var_dump(tree)
so = Solution()
so.recoverTree(tree)
var_dump(tree)
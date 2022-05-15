#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#

from collections import deque
from distutils.command.build import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
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

    def deepestLeavesSum(self, root: TreeNode) -> int:
        r = self.levelOrderIter(root)
        return sum(r[-1])

        
# @lc code=end

class Tree:
    def build(root: list[int]) -> TreeNode:
        
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


root = [1,2,3,4,5,None,6,7,None,None,None,None,8]
root = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]

tree = Tree.build(root)
so = Solution()
r = so.deepestLeavesSum(tree)
print(r)
#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
import pprint
from types import NoneType
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

    def postorder(self, root: TreeNode):

        if not root: return []

        r1 = self.postorder(root.left)
        if isinstance(r1, TreeNode):
            return r1
        elif (self.p.val in r1) and (self.q.val in r1): 
            return root.left

        r2 = self.postorder(root.right)
        if isinstance(r2, TreeNode):
            return r2
        elif (self.p.val in r2) and (self.q.val in r2): 
            return root.right

        r = r1 + r2 + [root.val]
        if (self.p.val in r) and (self.q.val in r):
            return root
        else:
            return r


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        return self.postorder(root)



        
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
        
    def preorder(self, root: TreeNode) -> list[int]:
        if not root: return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

    def preorderIter(self, root: TreeNode) -> list[int]:
        if not root: return []

        out = []
        q = deque()
        q.append(root)

        while q:
            node = q.pop()
            out.append(node.val)
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)

        return out

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

root = [3,5,1,6,2,0,8,None,None,7,4]
p = 5
q = 1

"""
root = [3,5,1,6,2,0,8,None,None,7,4]
p = 5
q = 4
"""

root = [1,2]
p = 1
q = 2

tree = Tree.build(root)
so = Solution()
r = so.lowestCommonAncestor(tree, TreeNode(p), TreeNode(q))
var_dump(r)

time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)
#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

from collections import deque
from functools import cache

from var_dump import var_dump


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start

class Solution:

    @cache
    def height(self, root: TreeNode) -> int:
        if not root: return -1
        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.height(root.left) - self.height(root.right)) <= 1 \
            and self.isBalanced(root.left) \
            and self.isBalanced(root.right)


    def isBalanced2(self, root: TreeNode) -> bool:
        if not root: return 1
        l = self.isBalanced(root.left)
        r = self.isBalanced(root.right)
        if not l or not r:
            return 0
        elif abs(l - r) <= 1:
            return max(l, r) + 1
        else:
            return 0
        
        
# @lc code=end


root = [3,9,20,None,None,15,7]
#root = [1,2,2,3,3,None,None,4,4]
#root = []
root = [1,2,2,3,None,None,3,4,None,None,4]

class BSTree:

    def __init__(self, ary: list[int]):

        self.head = None
        self.build(ary)

    def build(self, ary: list[int]) -> TreeNode:
        if not ary: 
            return None

        from collections import deque
        self.head = TreeNode(ary[0])        
        q = deque([self.head])

        for i in range(1, len(ary)):
            if i % 2 == 1:
                node = q.popleft()
                if ary[i]:
                    node.left = TreeNode(ary[i])
                    q.append(node.left)
            else:
                if ary[i]:
                    node.right = TreeNode(ary[i])
                    q.append(node.right)
        return self.head


bstree = BSTree(root)
#var_dump(bstree.head)

so = Solution()
r = so.isBalanced(bstree.head)
print(r)
from collections import deque
import math

from var_dump import var_dump


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if not root: return []

        out = -math.inf
        q = deque()
        curr = root

        while curr or q:
            while curr:
                q.append(curr)
                curr = curr.left
            curr = q.pop()
            if out == p.val: return curr
            out = curr.val
            curr = curr.right

        return None


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


root = [2,1,3]
p = 1

root = [5,3,6,2,4,None,None,1]
p = 6

tree = Tree.build(root)
so = Solution()
r = so.inorderSuccessor(tree, TreeNode(p))
var_dump(r)
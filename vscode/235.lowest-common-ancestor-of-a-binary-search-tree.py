#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

from var_dump import var_dump


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start

class Solution:
    def search(self, root: TreeNode, node: TreeNode) -> bool:
        
        if not root:
            return False
        
        elif node == root:
            return True

        elif node.val < root.val:
            return self.search(root.left, node)

        else:
            return self.search(root.right, node)


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p:
            return p
        elif root == q:
            return q

        pl = self.search(root.left, p)
        ql = self.search(root.left, q)

        if pl and ql:
            return self.lowestCommonAncestor(root.left, p, q)
        elif not pl and not ql:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
        
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


    def search(self, root: TreeNode, val: int) -> TreeNode:
        
        if not root or not root.val:
            return None
        
        elif val == root.val:
            return root

        elif val < root.val:
            return self.search(root.left, val)

        else:
            return self.search(root.right, val)


root = [6,2,8,0,4,7,9,None,None,3,5]
p = 2
q = 8

root = [6,2,8,0,4,7,9,None,None,3,5]
p = 2
q = 4


tr = Tree()
tree = Tree.build(root)

so = Solution()
r = so.lowestCommonAncestor(tree, tr.search(tree, p), tr.search(tree, q))
var_dump(r)
#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#
from var_dump import var_dump


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start

class Solution:

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        def successor(root: TreeNode) -> TreeNode:
            root = root.right
            while root.left:
                root = root.left
            return root

        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left and not root.right:
                return None

            if not root.left:
                return root.right

            if not root.right:
                return root.left

            ss = successor(root)
            root.val = ss.val
            root.right = self.deleteNode(root.right, root.val)

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


root = [5,3,6,2,4,None,7]
key = 3

root = [3,2,5,None,None,4,10,None,None,8,15,7]
key = 5

tree = Tree.build(root)
#var_dump(tree)
so = Solution()
r = so.deleteNode(tree, key)
var_dump(r)
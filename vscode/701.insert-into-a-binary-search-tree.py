#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#


from var_dump import var_dump


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        def insert(root: TreeNode, val: int):
            if val < root.val:
                if root.left:
                    root = root.left
                    insert(root, val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    root = root.right
                    insert(root, val)
                else:
                    root.right = TreeNode(val)

        if not root: return TreeNode(val)
        
        insert(root, val)
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


root = [40,20,60,10,30,50,70]
val = 25

tree = Tree.build(root)
so = Solution()
r = so.insertIntoBST(tree, val)
var_dump(r)
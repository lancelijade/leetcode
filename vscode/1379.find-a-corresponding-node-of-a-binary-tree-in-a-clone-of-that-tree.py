#
# @lc app=leetcode id=1379 lang=python3
#
# [1379] Find a Corresponding Node of a Binary Tree in a Clone of That Tree
#

from var_dump import var_dump

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        path = self.position_node(original, target)
        node = cloned
        for p in path:
            if p==1:
                node = node.left
            elif p==2:
                node = node.right
        return node


    # position the target in the tree, return the path, from the root, go 1 for left and 2 for right
    def position_node(self, tree: TreeNode, target: TreeNode) -> list[int]:
        if not tree: return None

        if tree == target:
            return []

        r = self.position_val(tree.left, target)
        if r is not None:
            return [1] + r
        
        r = self.position_val(tree.right, target)
        if r is not None:
            return [2] + r


    # position the target in the tree by TreeNode.val, return the path
    def position_val(self, tree: TreeNode, target: TreeNode) -> list[int]:
        if not tree: return None

        if tree.val == target.val:
            return []

        r = self.position_val(tree.left, target)
        if r is not None:
            return [1] + r
        
        r = self.position_val(tree.right, target)
        if r is not None:
            return [2] + r
        
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


tree = [7,4,3,None,None,6,19]
target = 3

original = Tree.build(tree)
cloned = Tree.build(tree)

so = Solution()
path = so.position_val(original, TreeNode(target))
#print(path)

cur = original
for pa in path:
    if pa==1:
        cur = cur.left
    elif pa==2:
        cur = cur.right
#print(cur)
#print(original.right.right)

r = so.getTargetCopy(original, cloned, cur)
print(r)
var_dump(r)
print(cloned.right)
#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
class Solution:

    def isValidBST2(self, root: TreeNode) -> bool:

        def isV(root: TreeNode) -> bool:
            
            if not root.left and not root.right: 
                return root.val, root.val

            elif root.left and not root.right:
                rll, rlr = isV(root.left)
                if not rll: 
                    return None, None
                if rlr < root.val:
                    return rll, root.val
                else:
                    return None, None

            elif not root.left and root.right:
                rrl, rrr = isV(root.right)
                if not rrl:
                    return None, None
                if root.val < rrl:
                    return root.val, rrr
                else:
                    return None, None

            else:
                rll, rlr = isV(root.left)
                rrl, rrr = isV(root.right)

                if rll is None or rrl is None: 
                    return None, None
                if rlr < root.val < rrl:
                    return rll, rrr
                else:
                    return None, None      

        r, _ = isV(root)
        return r is not None


    def isValidBST(self, root: TreeNode) -> bool:

        def valid(root: TreeNode, low: int, high: int) -> bool:

            if not root: return True
            if root.val<=low or root.val>=high: return False
            return valid(root.left, low, root.val) and valid(root.right, root.val, high)

        return valid(root, -math.inf, math.inf)
        
        
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

root = [5,1,4,None,None,3,6]
root = [2,1,3]
#root = [5,4,6,None,None,3,7]
#root = [1,1]
#root = [32,26,47,19,None,None,56,None,27]


tree = Tree.build(root)
so = Solution()
r = so.isValidBST(tree)
print(r)
#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def find(root: TreeNode) -> list:

            if not root.left and not root.right:
                return [root.val]

            ll, lr = [], []
            if root.left:
                ll = find(root.left)
            if root.right:
                lr = find(root.right)
            return ll + lr

        l1 = find(root1)
        l2 = find(root2)

        return l1 == l2
        
# @lc code=end


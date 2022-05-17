#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

from var_dump import var_dump

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:

        def genTree(start, end):
            #print(start, end)
            if start==end: return [TreeNode(start)]

            r = []
            for i in range(start, end+1):
                
                if i>start: treesLeft = genTree(start, i-1)
                else: treesLeft = [None]

                if i<end: treesRight = genTree(i+1, end)
                else: treesRight = [None]
                
                for trl in treesLeft:
                    for trr in treesRight:
                        root = TreeNode(i, trl, trr)
                        r.append(root)
            return r

        return genTree(1, n)    

        
# @lc code=end

n = 3
so = Solution()
r = so.generateTrees(n)
var_dump(r)
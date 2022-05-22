#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

from var_dump import var_dump


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        #rint(nums)
        le = len(nums)
        mid = int((le+1)/2)-1
        node = TreeNode(nums[mid])
        if mid>0: node.left = self.sortedArrayToBST(nums[:mid])
        if mid+1<le: node.right = self.sortedArrayToBST(nums[mid+1:])
        return node

        
# @lc code=end

nums = [-10,-3,0,5,9]
nums = [1,3]
nums = [3,5,8]

so = Solution()
r = so.sortedArrayToBST(nums)
var_dump(r)
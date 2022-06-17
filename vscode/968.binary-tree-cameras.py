#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
#

from var_dump import var_dump


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def minCameraCover(self, root):
        def solve(node):
            # 0: Strict ST; All nodes below this are covered, but not this one
            # 1: Normal ST; All nodes below and incl this are covered - no camera
            # 2: Placed camera; All nodes below this are covered, plus camera here

            if not node: return 0, 0, float('inf')
            L = solve(node.left)
            R = solve(node.right)

            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
            dp2 = 1 + min(L) + min(R)

            return dp0, dp1, dp2

        return min(solve(root)[1:])

        
# @lc code=end

class BSTree:
    
    def __init__(self, ary: list[int]):
        self.head = None
        self.build(ary)


    def build(self, ary: list[int]) -> TreeNode:
        if not ary: return None

        from collections import deque
        self.head = TreeNode(ary[0])        
        q = deque([self.head])

        for i in range(1, len(ary)):
            if i % 2 == 1:
                node = q.popleft()
                if ary[i] is not None:
                    node.left = TreeNode(ary[i])
                    q.append(node.left)
            else:
                if ary[i] is not None:
                    node.right = TreeNode(ary[i])
                    q.append(node.right)
        return self.head



root = [0,0,None,0,0]
root = [0,0,None,0,None,0,None,None,0]

tr = BSTree(root)
so = Solution()
r = so.minCameraCover(tr.head)
print(r)

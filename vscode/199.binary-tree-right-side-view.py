#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
from collections import deque

class Solution:

    def levelOrderIter(self, root: TreeNode) -> list[list[int]]:
        if not root: return []
        
        lvl = 0
        q = deque()
        q.append((root, lvl))
        r = []

        while q:
            node, lvl = q.popleft()
            if len(r)-1<lvl:
                r.append([])
            r[lvl].append(node.val)
            if node.left: q.append((node.left, lvl+1))
            if node.right: q.append((node.right, lvl+1))

        return r

    def rightSideView(self, root: TreeNode) -> list[int]:
        li = self.levelOrderIter(root)
        r = [x[-1] for x in li]
        return r


        
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


if __name__ == "__main__":
    
    root = [1,2,3,None,5,None,4]
    root = [1,None,3]
    root = []

    tree = BSTree(root)
    so = Solution()
    r = so.rightSideView(tree.head)
    print(r)
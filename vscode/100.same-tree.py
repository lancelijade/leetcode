#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
from collections import deque
from var_dump import var_dump


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start

class Solution:
    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p1, q1):
            if not p1 and not q1:
                return True
            if not p1 or not q1 or p1.val != q1.val:
                return False
            return True

        qe = deque([(p, q)])
        while qe:
            p1, q1 = qe.popleft()
            if not check(p1, q1):
                return False
            if p1 and q1:
                qe.append((p1.left, q1.left))
                qe.append((p1.right, q1.right))
        return True

        
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
                if ary[i]:
                    node.left = TreeNode(ary[i])
                    q.append(node.left)
            else:
                if ary[i]:
                    node.right = TreeNode(ary[i])
                    q.append(node.right)
        return self.head


p = [1,2,3]
q = [1,2,3]

tp = BSTree(p)
tq = BSTree(q)
so = Solution()
r = so.isSameTree(tp.head, tq.head)
print(r)
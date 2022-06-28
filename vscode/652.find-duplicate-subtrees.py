#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#

from collections import defaultdict
from var_dump import var_dump


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> list[TreeNode]:
        
        def st(node: TreeNode) -> list[int]:
            if not node:
                return None
            r = (node.val, st(node.left), st(node.right))
            d[r] += 1
            dd[r] = node
            return r
            
        d = defaultdict(int)
        dd = defaultdict(tuple)
        st(root)
        #print(d, dd)

        r = []
        for k, v in d.items():
            if v > 1:
                r.append(dd[k])

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



root = [1,2,3,4,None,2,4,None,None,4]


bst = BSTree(root)
so = Solution()
r = so.findDuplicateSubtrees(bst.head)
var_dump(r)
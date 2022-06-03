from var_dump import var_dump


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList1(self, root: Node) -> Node:
        
        def inorder(root: Node) -> list[int]:
            if not root: return []
            return inorder(root.left) + [root] + inorder(root.right)

        if not root: return None
        l = inorder(root)
        le = len(l)
        for i in range(le):
            if i < le-1:
                l[i].right = l[i+1]
            if i > 0:
                l[i].left = l[i-1]
        l[0].left = l[le-1]
        l[le-1].right = l[0]

        return l[0]

    def treeToDoublyList(self, root: Node) -> Node:
        
        def helper(node: Node):
            nonlocal first, last

            if not node: return

            helper(node.left)

            if last:
                last.right = node
                node.left = last
            else:
                first = node
            last = node

            helper(node.right)

        first, last = None, None
        helper(root)
        if first:
            first.left = last
            last.right = first
        return first



class BSTree:
    def __init__(self, ary: list[int]):
        self.head = None
        self.build(ary)


    def build(self, ary: list[int]) -> Node:
        if not ary: return None

        from collections import deque
        self.head = Node(ary[0])        
        q = deque([self.head])

        for i in range(1, len(ary)):
            if i % 2 == 1:
                node = q.popleft()
                if ary[i]:
                    node.left = Node(ary[i])
                    q.append(node.left)
            else:
                if ary[i]:
                    node.right = Node(ary[i])
                    q.append(node.right)
        return self.head


root = [4,2,5,1,3]
#root = []

tree = BSTree(root)
so = Solution()
r = so.treeToDoublyList(tree.head)
var_dump(r)
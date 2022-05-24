
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


    '以下方法独立调用, 不自动使用 self.head'
    from functools import cache
    @cache
    def height(self, root: TreeNode) -> int:
        if not root: return -1
        return max(self.height(root.left), self.height(root.right)) + 1


    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.height(root.left) - self.height(root.right)) <= 1 \
            and self.isBalanced(root.left) \
            and self.isBalanced(root.right)


    def insert(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)

        if val < root.val:
            if root.left:
                root.left = self.insert(root.left, val)
            else:
                root.left = TreeNode(val)
        else:
            if root.right:
                root.right = self.insert(root.right, val)
            else:
                root.right = TreeNode(val)
        
        return root


    def delete(self, root: TreeNode, key: int) -> TreeNode:
    
        def successor(root: TreeNode) -> TreeNode:
            root = root.right
            while root.left:
                root = root.left
            return root

        if not root:
            return None
        
        if key < root.val:
            root.left = self.delete(root.left, key)

        elif key > root.val:
            root.right = self.delete(root.right, key)

        else:
            if not root.left and not root.right:
                return None

            if not root.left:
                return root.right

            if not root.right:
                return root.left

            ss = successor(root)
            root.val = ss.val
            root.right = self.delete(root.right, root.val)

        return root


    def search(self, root: TreeNode, val: int) -> TreeNode:
        if not root or not root.val: 
            return None
        elif val == root.val:
            return root
        elif val < root.val:
            return self.search(root.left, val)
        else:
            return self.search(root.right, val)
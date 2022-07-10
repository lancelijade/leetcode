
class Solution:
    def inorderSuccessor(self, node, last=None):

        if node.right and node.right != last:
            r = node.right
            while r.left:
                r = r.left
            return r

        r = node.parent
        if not r: return None
        if r.left == node: return r

        return self.inorderSuccessor(r, node)       




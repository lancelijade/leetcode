from collections import deque
from var_dump import var_dump


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Codec:
    # binary tree builder
    def BTreeBuild(self, root: list[int]) -> TreeNode:
        if not root: return None

        le = len(root)

        a = []
        for val in root:
            if val is None: node = None
            else: node = TreeNode(val)
            a.append(node)

        i = 0
        j = 1
        while j < le:
            if a[i]:
                if a[j]: 
                    a[i].left = a[j]
                j += 1

                if j == le: break
                
                if a[j]:
                    a[i].right = a[j]
                j += 1

            i += 1

        return a[0]


    # N-Tree builder
    def NtreeBuild(self, root: list[int]) -> Node:
        if not root: return None

        le = len(root)

        q = deque()
        head = Node(root[0], [])
        q.append(head)

        i = 2

        while q:
            chead = q.popleft()
            while i<le:
                n = root[i]
                i += 1
                if n is None:
                    break
                if not chead.children:
                    chead.children = []
                cur = Node(n, [])
                chead.children.append(cur)
                q.append(cur)

        return head


    # binary tree level order traversal
    def BTreelevelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root: return []

        lvl = 0
        q = deque()
        q.append((root, lvl))
        r = []

        while q:
            node, lvl = q.popleft()
            if not node:
                r.append(None)
                continue
            r.append(node.val)
            q.append((node.left, lvl+1))
            q.append((node.right, lvl+1))

        # trim tail None
        for j in range(len(r)-1, 0, -1):
            if r[j] is not None: break

        return r[:j+1]


    # N-Tree level order traversal
    def NTreelevelOrder(self, root: Node) -> list[list[int]]:
        if not root: return []

        lvl = 0
        q = deque()
        q.append((root, lvl))
        q.append((None, lvl))
        r = []

        while q:
            node, lvl = q.popleft()
            if not node:
                r.append(None)
                continue
            r.append(node.val)
            if not node.children:
                q.append((None, lvl+1))
            else:
                for nn in node.children:
                    q.append((nn, lvl+1))
                q.append((None, lvl+1))

        # trim tail None
        for j in range(len(r)-1, 0, -1):
            if r[j] is not None: break

        return r[:j+1]


    def encode(self, root: Node) -> TreeNode:
        ary = self.NTreelevelOrder(root)
        return self.BTreeBuild(ary)


    def decode(self, data: TreeNode) -> Node:
        ary = self.BTreelevelOrder(data)
        return self.NtreeBuild(ary)


root = [1,None,3,2,4,None,5,6]
#root = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
#root = []
root = [1,None,10,3,None,5,0,None,6]


codec = Codec()
tree = codec.NtreeBuild(root)
en = codec.encode(tree)
#var_dump(en)
r = codec.decode(en)
var_dump(r)



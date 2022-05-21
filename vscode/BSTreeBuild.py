from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


"ListNode"
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def buildList(root: list[int]) -> ListNode:
    head = ListNode(0)
    h = head
    for n in root:
        node = ListNode(n)
        h.next = node
        h = h.next
    return head.next



def BSTreeBuild(root: list[int]) -> TreeNode:
    
    if not root: return None

    le = len(root)

    a = []
    for val in root:
        if val is None: node = None
        else: node = TreeNode(val)
        a.append(node)

    h = a[0]
    i = 1
    while i < le:
        if not a[i]:
            i += 1
            continue

        if a[i].val < h.val:
            if not h.left:
                h.left = a[i]
            else:
                h = h.left
                continue
        else:
            if not h.right:
                h.right = a[i]
            else:
                h = h.right
                continue

        h = a[0]
        i += 1

    return a[0]


def hardBSTreeBuild(root: list[int]) -> TreeNode:
    
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


class Tree:

    def build(root: list[int]) -> TreeNode:
        
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


    def search(self, root: TreeNode, val: int) -> TreeNode:
    
        if not root or not root.val:
            return None
        
        elif val == root.val:
            return root

        elif val < root.val:
            return self.search(root.left, val)

        else:
            return self.search(root.right, val)


    def preorder(self, root: TreeNode) -> list[int]:
        if not root: return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

    def preorderIter(self, root: TreeNode) -> list[int]:
        if not root: return []

        out = []
        q = deque()
        q.append(root)

        while q:
            node = q.pop()
            out.append(node.val)
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)

        return out

    def inorder(self, root: TreeNode) -> list[int]:
        if not root: return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def inorderIter(self, root: TreeNode) -> list[int]:
        if not root: return []

        out = []
        q = deque()
        curr = root

        while curr or q:
            while curr:
                q.append(curr)
                curr = curr.left
            curr = q.pop()
            out.append(curr.val)
            curr = curr.right

        return out        

    def postorder(self, root: TreeNode) -> list[int]:
        if not root: return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.val]

    def postorderIter(self, root: TreeNode) -> list[int]:
        if not root: return []

        res = []
        stack = deque()
        node = root
        last_visited_node = None

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            # no right subtree, right subtree was visited
            if stack[-1].right in [None, last_visited_node]:
                res.append(stack[-1].val)
                last_visited_node = stack.pop()
                
            # right subtree was not visited
            else:
                node = stack[-1].right

        return res

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
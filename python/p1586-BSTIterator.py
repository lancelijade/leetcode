import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.vals = []
        self.lnr(root)
        self.p = -1
        self.length = len(self.vals)

    def lnr(self, root: TreeNode):
        if root.left: self.lnr(root.left)
        self.vals.append(root.val)
        if root.right: self.lnr(root.right)

    def hasNext(self) -> bool:
        if self.p<self.length-1: return True
        else: return False

    def next(self) -> int:
        self.p += 1
        return self.vals[self.p]

    def hasPrev(self) -> bool:
        if self.p>0: return True
        else: return False

    def prev(self) -> int:
        self.p -= 1
        return self.vals[self.p]


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()

root = [7, 3, 15, None, None, 9, 20]

tree = BSTreeBuild(root)
it = BSTIterator(tree)
var_dump(it)
print(it.next())
print(it.next())
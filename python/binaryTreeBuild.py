import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeBuild(root: list[int]) -> TreeNode:

    le = len(root)

    a = []
    for val in root:
        node = TreeNode(val)
        a.append(node)
    #var_dump(a)

    for i, node in enumerate(a):
        if i*2+1 < le: node.left = a[i*2+1]
        if i*2+2 < le: node.right = a[i*2+2]

    return a[0]



root = [4,2,7,1,3,None,12]
val = 2

r = treeBuild(root)
var_dump(r)
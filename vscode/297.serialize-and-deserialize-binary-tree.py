#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
class Codec:

    def build(self, root: list[int]) -> TreeNode:
        
        if not root: return None

        le = len(root)

        a = []
        for val in root:
            if val is None or val == "None": node = None
            else: node = TreeNode(int(val))
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

    def levelOrderIter(self, root: TreeNode) -> list[list[int]]:
        if not root: return []
        
        lvl = 0
        q = deque()
        q.append((root, lvl))
        r = []

        while q:
            node, lvl = q.popleft()
            if not node:
                r.append("None")
                continue

            r.append(str(node.val))
            q.append((node.left, lvl+1))
            q.append((node.right, lvl+1))

        return r

    def serialize(self, root: TreeNode) -> str:
        if not root: return ""
        l = self.levelOrderIter(root)
        r = ','.join(l)
        return r

    def deserialize(self, data: str) -> TreeNode:
        if not data: return None
        l = data.split(',')
        return self.build(l)


# @lc code=end

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

root = [1,2,3,None,None,4,5]
root = []

tree = hardBSTreeBuild(root)
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(tree))
var_dump(ans)
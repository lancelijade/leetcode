#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#
import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump
from collections import defaultdict
import math
import heapq
from collections import deque
from datetime import datetime 
time_start = datetime.now()

# @lc code=start
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:

    def levelOrderIter(self, root: Node):
        if not root: return
        
        q = deque()
        if root.left: q.append((root.left, 1))
        if root.right: q.append((root.right, 1))

        lvl_last = 0
        node_last = root

        while q:
            node, lvl = q.popleft()
            if lvl == lvl_last:
                node_last.next = node
                node_last = node
            else:
                lvl_last = lvl
                node_last = node
            if node.left: q.append((node.left, lvl+1))
            if node.right: q.append((node.right, lvl+1))


    def connect(self, root: 'Node') -> 'Node':
        self.levelOrderIter(root)
        return root

# @lc code=end


def hardBSTreeBuild(root: list[int]) -> Node:
    
    if not root: return None

    le = len(root)

    a = []
    for val in root:
        if val is None: node = None
        else: node = Node(val)
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
    
root = [1,2,3,4,5,None,7]

tree = hardBSTreeBuild(root)
#var_dump(tree)
so = Solution()
r = so.connect(tree)
var_dump(r)

time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)
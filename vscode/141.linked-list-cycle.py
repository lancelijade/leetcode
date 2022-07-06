#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

from var_dump import var_dump


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @lc code=start
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        sstep = 1
        fstep = 2

        slow = head
        fast = head

        while slow and fast:
            #print(slow.val, fast.val)

            if not slow.next:
                return False
            slow = slow.next
            
            if not fast.next or not fast.next.next:
                return False
            fast = fast.next.next

            if slow == fast:
                return True

        return False
        
    
# @lc code=end


head = [3,2,0,-4]
pos = 1

head = [1,2]
pos = 0

head = [1]
pos = -1

head = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
pos = -1

hd = ListNode(0)
cur = hd
cy = None
for i in range(len(head)):
    node = ListNode(head[i])
    if i == pos:
        cy = node
    cur.next = node
    cur = cur.next
cur.next = cy
#var_dump(hd.next)

so = Solution()
r = so.hasCycle(hd.next)
print(r)

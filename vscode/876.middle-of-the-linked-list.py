#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#
from var_dump import var_dump


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# @lc code=start
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p1, p2 = head, head
        while p1:
            if p1.next:
                p1 = p1.next.next
                p2 = p2.next
            else:
                return p2
        return p2
        

# @lc code=end

head = [1,2,3,4,5,6]
head = [1,2,3,4,5]

hd = ListNode(-1)
h = hd
for n in head:
    node = ListNode(n)
    h.next = node
    h = h.next
h = hd.next

#var_dump(h)

so = Solution()
r = so.middleNode(h)
var_dump(r)
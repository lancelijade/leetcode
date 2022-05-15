#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

from var_dump import var_dump


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def rev(head):
            if not head.next: return [head, head]
            if not head.next.next:
                n2 = head.next
                n2.next = head
                head.next = None
                return [n2, head]
            
            h, e = rev(head.next)
            e.next = head
            head.next = None
            return [h, head]

        if not head: return None
        h, e = rev(head)
        return h

        
# @lc code=end

def buildList(root: list[int]) -> ListNode:
    head = ListNode(0)
    h = head
    for n in root:
        node = ListNode(n)
        h.next = node
        h = h.next
    return head.next

head = [1,2,3,4,5]
#head = [1,2]
#head = [1]

li = buildList(head)
so = Solution()
r = so.reverseList(li)
var_dump(r)
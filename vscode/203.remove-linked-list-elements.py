#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
from var_dump import var_dump


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next

        if not head: return

        slow, fast = head, head.next
        while slow and fast:
            if fast.val == val:
                slow.next = fast.next
                fast = fast.next
            else:
                slow = slow.next
                fast = fast.next

        return head

        
# @lc code=end

if __name__ == "__main__":

    head = [1,2,6,3,4,5,6]
    val = 6

    head = []
    val = 1

    head = [7,7,7,7]
    val = 7

    tree = ListNode(0)
    h = tree
    for i in head:
        node = ListNode(i)
        h.next = node
        h = h.next

    so = Solution()
    r = so.removeElements(tree.next, val)
    var_dump(r)
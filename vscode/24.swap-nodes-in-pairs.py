#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

from var_dump import var_dump


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        n2 = head.next
        n3 = head.next.next
        head.next = n3
        n2.next = head
        n2.next.next = self.swapPairs(n3)
        return n2

        
# @lc code=end


def buildList(root: list[int]) -> ListNode:
    head = ListNode(0)
    h = head
    for n in root:
        node = ListNode(n)
        h.next = node
        h = h.next
    return head.next


head = [1,2,3,4]
head = []
head = [1]

li = buildList(head)
so = Solution()
r = so.swapPairs(li)
var_dump(r)

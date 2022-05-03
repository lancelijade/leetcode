import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def makeList(li: list[int]) -> list[int]:
    head = ListNode(0)
    h = head
    for i in range(len(li)):
        node = ListNode(li[i])
        h.next = node
        h = h.next
    return head.next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        head = ListNode(0)
        h = head
        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val<=p2.val:
                h.next = p1
                p1 = p1.next
                h = h.next
            else:
                h.next = p2
                p2 = p2.next
                h = h.next

        h.next = p1 if p1 is not None else p2

        return head.next



list1 = [1,2,4]
list2 = [1,3,4]
#list1 = []
#list2 = []
#list1 = []
#list2 = [0]

l1 = makeList(list1)
l2 = makeList(list2)
so = Solution()
r = so.mergeTwoLists(l1, l2)
#pp.pprint(r)
var_dump(r)
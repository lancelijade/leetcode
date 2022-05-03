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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode(0)
        h = head
        a0 = 0

        while l1 or l2:
            summ = 0
            if l1: summ += l1.val
            if l2: summ += l2.val
            a, b = divmod(summ + a0, 10)
            node = ListNode(val=b, next=h.next)
            a0 = a
            h.next = node
            h = h.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if a0:
            node = ListNode(val=a0, next=h.next)
            h.next = node

        return head.next


l1 = [2,4,3]
l2 = [5,6,4]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

list1 = makeList(l1)
list2 = makeList(l2)
#print(list1)
so = Solution()
r = so.addTwoNumbers(list1, list2)
var_dump(r)


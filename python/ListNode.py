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
    pass



l1 = [2,4,3]
l2 = [5,6,4]

list1 = makeList(l1)
list2 = makeList(l2)

so = Solution()
r = so.addTwoNumbers(list1, list2)
var_dump(r)


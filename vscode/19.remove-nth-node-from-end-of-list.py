#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
from var_dump import var_dump


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow, fast = head, head
        while n > 0:
            if fast:
                fast = fast.next
                n -= 1
            else:
                return None

        i = 0
        while fast:
            fast = fast.next
            i += 1

        if i > 0:
            while i > 1:
                slow = slow.next
                i -= 1
            slow.next = slow.next.next
        else:
            head = slow.next

        return head
        

        
# @lc code=end


if __name__ == "__main__":

    head = [1,2,3,4,5]
    n = 2

    
    head = [1]
    n = 1
    
    
    head = [1,2]
    n = 1

    
    head = [1,2]
    n = 2
    ''''''

    tree = ListNode(0)
    h = tree
    for i in head:
        node = ListNode(i)
        h.next = node
        h = h.next

    so = Solution()
    r = so.removeNthFromEnd(tree.next, n)
    var_dump(r)
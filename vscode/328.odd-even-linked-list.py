#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

from var_dump import var_dump


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd, even = head, head.next
        estart = even

        while odd.next and even.next:
            #print(odd.val, even.val)
            odd.next = even.next
            odd = odd.next
            if odd.next:
                even.next = odd.next
                even = even.next

        odd.next = estart
        even.next = None
        return head

        
# @lc code=end

if __name__ == "__main__":

    head = [1,2,3,4,5]
    head = [2,1,3,5,6,4,7]

    tree = ListNode(0)
    h = tree
    for i in head:
        node = ListNode(i)
        h.next = node
        h = h.next

    so = Solution()
    r = so.oddEvenList(tree.next)
    var_dump(r)
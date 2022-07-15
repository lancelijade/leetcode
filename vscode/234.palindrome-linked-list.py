#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

from var_dump import var_dump


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        li = []
        while head:
            li.append(head.val)
            head = head.next

        return li == list(reversed(li))

        
# @lc code=end

if __name__ == "__main__":
    
    head = [1,2,2,1]

    tree = ListNode(0)
    h = tree
    for i in head:
        node = ListNode(i)
        h.next = node
        h = h.next

    so = Solution()
    r = so.isPalindrome(tree.next)
    var_dump(r)
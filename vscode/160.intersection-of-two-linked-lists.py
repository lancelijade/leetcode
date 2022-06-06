#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @lc code=start

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha = headA
        hb = headB
        
        while ha != hb:
            ha = headB if ha is None else ha.next
            hb = headA if hb is None else hb.next

        return ha
        
        
# @lc code=end


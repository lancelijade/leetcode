#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

from var_dump import var_dump

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @lc code=start
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        d = {}
        cur = head

        while cur:
            if cur in d:
                return d[cur]
            d[cur] = cur
            cur = cur.next

        return None

        
# @lc code=end

if __name__ == "__main__":

    head = [3,2,0,-4]
    pos = 1


    head = [1,2]
    pos = 0
    '''
    head = [1]
    pos = -1

    head = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
    pos = -1
    '''

    hd = ListNode(0)
    cur = hd
    cy = None
    for i in range(len(head)):
        node = ListNode(head[i])
        if i == pos:
            cy = node
        cur.next = node
        cur = cur.next
    cur.next = cy
    #var_dump(hd.next)

    so = Solution()
    r = so.detectCycle(hd.next)
    print(r)
#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
from var_dump import var_dump

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def buildList(root: list[int]) -> ListNode:
    head = ListNode(0)
    h = head
    for n in root:
        node = ListNode(n)
        h.next = node
        h = h.next
    return head.next

# @lc code=start

class Solution:
    def mergeTwoLists_iter(self, list1: ListNode, list2: ListNode) -> ListNode:
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


    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        if not list1: return list2
        if not list2: return list1

        if list1.val<list2.val:
            r = self.mergeTwoLists(list1.next, list2)
            list1.next = r
            return list1
        else:
            r = self.mergeTwoLists(list1, list2.next)
            list2.next = r
            return list2


# @lc code=end

def log(func):
    def wrapper(*args, **kw):
        from datetime import datetime 
        time_start = datetime.now()
        #print('call %s():' % func.__name__)
        r = func(*args, **kw)
        time_end = datetime.now()
        print("---\ntime cost:",time_end-time_start)
        return r
    return wrapper

@log
def run(*args, **kw):
    so = Solution()
    r = so.mergeTwoLists(*args, **kw)
    var_dump(r)


list1 = [1,2,4]
list2 = [1,3,4]

run(buildList(list1), buildList(list2))
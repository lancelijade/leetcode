#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#
from var_dump import var_dump

# @lc code=start
class Node:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def get(self, index: int) -> int:
        if index >= self.len:
            return -1
        else:
            hd = self.head
            while index > 0:
                hd = hd.next
                index -= 1
            return hd.val

    def addAtHead(self, val: int) -> None:
        head = Node(val, self.head)
        self.head = head
        self.len += 1

    def addAtTail(self, val: int) -> None:
        if self.len == 0:
            return self.addAtHead(val)
        else:
            hd = self.head
            while hd.next:
                hd = hd.next
            node = Node(val)
            hd.next = node
            self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            return self.addAtHead(val)
        elif index == self.len:
            return self.addAtTail(val)
        elif index > self.len:
            return
        else:
            hd = self.head
            while index > 1:
                hd = hd.next
                index -= 1
            node = Node(val, hd.next)
            hd.next = node
            self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.len:
            return
        elif index == 0:
            self.head = self.head.next
            self.len -= 1
        else:
            hd = self.head
            while index > 1:
                hd = hd.next
                index -= 1
            hd.next = hd.next.next
            self.len -= 1


# @lc code=end

in1 = ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
in2 = [[], [1], [3], [1, 2], [1], [1], [1]]

in1 = ["MyLinkedList","addAtHead","deleteAtIndex"]
in2 = [[],[1],[0]]

in1 = ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
in2 = [[],[1],[3],[1,2],[1],[2],[0]]

in1 = ["MyLinkedList","addAtIndex","addAtIndex","addAtIndex","get"]
in2 = [[],[0,10],[0,20],[1,30],[0]]

in1 = ["MyLinkedList","addAtTail","get"]
in2 = [[],[1],[0]]

in1 = ["MyLinkedList","addAtHead","get","addAtHead","addAtHead","deleteAtIndex","addAtHead","get","get","get","addAtHead","deleteAtIndex"]
in2 = [[],[4],[1],[1],[5],[3],[7],[3],[3],[3],[1],[4]]

in1 = ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get","get","deleteAtIndex","deleteAtIndex","get","deleteAtIndex","get"]
in2 = [[],[1],[3],[1,2],[1],[1],[1],[3],[3],[0],[0],[0],[0]]

o = None
cmd = []
ret = [None]
if in2[0]:
    cmd.append('o = {}({})'.format(in1[0], in2[0][0]))
else:
    cmd.append('o = {}()'.format(in1[0]))

for i in range(1, len(in1)):
    if len(in2[i])>0:
        msg = ",".join(map(str, in2[i]))
        cmd.append('ret.append(o.{}({}))'.format(in1[i], msg))
    else:
        cmd.append('ret.append(o.{}())'.format(in1[i]))

for cmdd in cmd:
    print(cmdd)
    exec(cmdd)
    var_dump(o)
    print("=====\n")

print(ret)
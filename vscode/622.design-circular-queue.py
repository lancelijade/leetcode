#
# @lc app=leetcode id=622 lang=python3
#
# [622] Design Circular Queue
#

from collections import defaultdict
from var_dump import var_dump
import pprint
pp = pprint.PrettyPrinter()
from datetime import datetime 
time_start = datetime.now()

# @lc code=start
class MyCircularQueue:

    def __init__(self, k: int):
        self.c = [0] * k
        self.size = k
        self.head = 0
        self.tail = 0
        self.cnt = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.c[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        self.cnt += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = (self.head + 1) % self.size
        self.cnt -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.c[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        t = (self.tail + self.size - 1) % self.size
        return self.c[t]

    def isEmpty(self) -> bool:
        return self.cnt == 0

    def isFull(self) -> bool:
        return self.cnt == self.size


# @lc code=end

in1 = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
in2 = [[3], [1], [2], [3], [4], [], [], [], [4], []]

o = None
ret = [None]
exec('o = {}({})'.format(in1[0], in2[0][0]))

for i in range(1, len(in1)):
    if (len(in2[i])>0):
        exec('ret.append(o.{}({}))'.format(in1[i], in2[i][0]))
    else:
        exec('ret.append(o.{}())'.format(in1[i]))

print(ret)


time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)
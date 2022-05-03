#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.cur = self.q1
        self.oth = self.q2
        self.now = None

    def oth_to_cur(self):
        while self.oth:
            self.cur.append(self.oth.popleft())

    def push(self, x: int) -> None:
        self.oth_to_cur()
        self.cur, self.oth = self.oth, self.cur
        self.cur.append(x)

    def pop(self) -> int:
        if self.cur:
            return self.cur.popleft()
        else:
            return self.oth.popleft()

    def top(self) -> int:
        if self.cur:
            return self.cur[0]
        else:
            return self.oth[0]

    def empty(self) -> bool:
        return not self.cur and not self.oth



# @lc code=end

in1 = ["MyStack", "push", "push", "top", "pop", "empty"]
in2 = [[], [1], [2], [], [], []]

o = None
ret = [None]
if in2[0]:
    exec('o = {}({})'.format(in1[0], in2[0][0]))
else:
    exec('o = {}()'.format(in1[0]))

for i in range(1, len(in1)):
    if (len(in2[i])>0):
        exec('ret.append(o.{}({}))'.format(in1[i], in2[i][0]))
    else:
        exec('ret.append(o.{}())'.format(in1[i]))

print(ret)
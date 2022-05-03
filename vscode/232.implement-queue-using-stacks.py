#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#
from datetime import datetime 
time_start = datetime.now()

# @lc code=start
class MyQueue:

    def __init__(self):
        self.a = [[], []]
        self.st = 0
        self.q = 1

    def st_to_q(self):
        while self.a[self.st]:
            self.a[self.q].append(self.a[self.st].pop())

    def push(self, x: int) -> None:
        self.a[self.st].append(x)

    def pop(self) -> int:
        if not self.a[self.q]:
            self.st_to_q()
        return self.a[self.q].pop()

    def peek(self) -> int:
        if not self.a[self.q]:
            self.st_to_q()
        return self.a[self.q][-1]

    def empty(self) -> bool:
        return not self.a[self.st] and not self.a[self.q]


# @lc code=end


in1 = ["MyQueue", "push", "push", "peek", "pop", "empty"]
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

time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)
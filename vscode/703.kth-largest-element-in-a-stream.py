#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.q = heapq.nlargest(k, nums)
        heapq.heapify(self.q)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.q)>=self.k:
            heapq.heappushpop(self.q, val)
        else:
            heapq.heappush(self.q, val)
        return self.q[0]


# @lc code=end

in1 = ["KthLargest", "add", "add", "add", "add", "add"]
in2 = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

in1 = ["KthLargest","add","add","add","add","add"]
in2 = [[1,[]],[-3],[-2],[-4],[0],[4]]

o = None
ret = [None]
if in2[0]:
    exec('o = {}({}, {})'.format(in1[0], in2[0][0], in2[0][1]))
else:
    exec('o = {}()'.format(in1[0]))

for i in range(1, len(in1)):
    if (len(in2[i])>0):
        exec('ret.append(o.{}({}))'.format(in1[i], in2[i][0]))
    else:
        exec('ret.append(o.{}())'.format(in1[i]))

print(ret)
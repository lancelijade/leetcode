#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import bisect


class MedianFinder:

    def __init__(self):
        self.a = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.a, num)

    def findMedian(self) -> float:
        n = len(self.a)
        if n % 2 == 1:
            return self.a[n//2]
        else:
            return (self.a[n//2-1]+self.a[n//2])/2



# @lc code=end

in1 = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
in2 = [[], [1], [2], [], [3], []]

in1 = ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
in2 = [[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]

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
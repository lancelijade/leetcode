#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import bisect
import heapq


" insort "
class MedianFinder2:

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


" two heaps "
class MedianFinder:
    
    def __init__(self):
        self.hp_left = []       # numbers < median
        self.hp_right = []      # numbers > median

    def rebalance(self) -> None:
        len1 = len(self.hp_left)
        len2 = len(self.hp_right)
        if len1 - len2 > 1:
            num = -heapq.heappop(self.hp_left)
            heapq.heappush(self.hp_right, num)
        elif len2 - len1 > 1:
            num = heapq.heappop(self.hp_right)
            heapq.heappush(self.hp_left, -num)

    def addNum(self, num: int) -> None:
        if not self.hp_left or num < -self.hp_left[0]:      
            heapq.heappush(self.hp_left, -num)
        else:
            heapq.heappush(self.hp_right, num)

        self.rebalance()
        #print(num, self.hp_left, self.hp_right)

    def findMedian(self) -> float:
        len1 = len(self.hp_left)
        len2 = len(self.hp_right)
        if len1 == len2:
            return (-self.hp_left[0] + self.hp_right[0])/2
        elif len1 > len2:
            return -self.hp_left[0]
        else:
            return self.hp_right[0]


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
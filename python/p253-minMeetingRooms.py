import heapq

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        tb = []
        heapq.heapify(tb)
        for a,b in intervals:
            heapq.heappush(tb, (a, 1))
            heapq.heappush(tb, (b, -1))

        ma = 0
        r = 0
        while tb:
            mn, d = heapq.heappop(tb)
            r += d
            ma = max(ma, r)

        return ma


intervals = [[0,30],[5,10],[15,20]]
intervals = [[7,10],[2,4]]

so = Solution()
r = so.minMeetingRooms(intervals)
print(r)
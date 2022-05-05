import heapq

class Solution:
    def connectSticks(self, sticks: list[int]) -> int:
        heapq.heapify(sticks)
        r = 0
        while len(sticks)>1:
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            r += a+b
            heapq.heappush(sticks, a+b)
        return r


sticks = [2,4,3]
sticks = [1,8,3,5]

so = Solution()
r = so.connectSticks(sticks)
print(r)
#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        sts = [-x for x in stones]
        heapq.heapify(sts)

        while len(sts)>1:
            x = -heapq.heappop(sts)
            y = -heapq.heappop(sts)
            if x<y:
                heapq.heappush(sts, -y+x)
            elif y<x:
                heapq.heappush(sts, -x+y)
        
        if sts:
            return -sts[0]
        else:
            return 0


# @lc code=end

stones = [2,7,4,1,8,1]
stones = [1]
stones = [2,2]

so = Solution()
r = so.lastStoneWeight(stones)
print(r)
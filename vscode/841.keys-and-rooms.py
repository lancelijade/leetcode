#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        q = deque()
        seen = [False] * len(rooms)
        seen[0] = True
        
        for n in rooms[0]:
            q.append(n)
            #seen[n] = True

        while q:
            n = q.popleft()
            seen[n] = True
            for x in rooms[n]:
                if not seen[x]:
                    q.append(x)

        #print(seen)
        return False not in seen

        
# @lc code=end

rooms = [[1],[2],[3],[]]
rooms = [[1,3],[3,0,1],[2],[0]]

so = Solution()
r = so.canVisitAllRooms(rooms)
print(r)
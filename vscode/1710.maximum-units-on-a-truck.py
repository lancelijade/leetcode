#
# @lc app=leetcode id=1710 lang=python3
#
# [1710] Maximum Units on a Truck
#

# @lc code=start
class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        bt = sorted(boxTypes, key=lambda x:x[1], reverse=True)
        #print(bt)

        rn = 0
        r = 0
        for n, cnt in bt:
            if n + rn <= truckSize:
                rn += n
                r += n * cnt
            else:
                r += (truckSize - rn) * cnt
                break
            #print(rn, r, n, cnt)

        return r

        
# @lc code=end

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10

boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4

so = Solution()
r = so.maximumUnits(boxTypes, truckSize)
print(r)
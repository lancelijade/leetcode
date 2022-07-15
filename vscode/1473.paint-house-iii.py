#
# @lc app=leetcode id=1473 lang=python3
#
# [1473] Paint House III
#

# @lc code=start
from functools import cache
import math


class Solution:
    def minCost(self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int) -> int:
        
        @cache
        def dp(i, color, color_before, cost_before, nb_before) -> int:

            #print(i, color, cost_before, nb_before)

            if i >= size:
                if nb_before == target:
                    return cost_before
                else:
                    return -1

            if nb_before > target:
                return -1

            if i > 0:
                nbnow = nb_before if color == color_before else nb_before + 1
            else:
                nbnow = 1

            if houses[i] == 0:
                costnow = cost_before + cost[i][color-1]
            else:
                costnow = cost_before

            minc = math.inf
            if i + 1 < size:
                if houses[i+1] == 0:
                    for j in range(n):
                        co = dp(i+1, j+1, color, costnow, nbnow)
                        if co != -1:
                            minc = min(minc, co)
                    return minc if minc != math.inf else -1
                else:
                    return dp(i+1, houses[i+1], color, costnow, nbnow)

            else:
                if nbnow == target:
                    return costnow
                else:
                    return -1

            
        size = len(houses)
        
        if houses[0] == 0:
            minc = math.inf
            for j in range(n):
                co = dp(0, j+1, -1, 0, 1)
                if co != -1:
                    minc = min(minc, co)
            return minc if minc != math.inf else -1
        else:
            return dp(0, houses[0], -1, 0, 1)
        
        
# @lc code=end


if __name__ == "__main__":
    
    houses = [0,0,0,0,0]
    cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
    m = 5
    n = 2
    target = 3

    '''
    houses = [0,2,1,2,0]
    cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
    m = 5
    n = 2
    target = 3

    houses = [3,1,2,3]
    cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
    m = 4
    n = 3
    target = 3

    '''

    houses = [0,5,0,3,2,1,0,5,3,1,4,2,0,0,2,3]
    cost = [[7,3,6,11,18],[15,9,11,10,15],[12,10,18,14,4],[7,19,17,4,20],[8,8,20,17,1],[19,18,19,8,1],[14,16,6,13,15],[16,1,20,17,14],[4,6,4,10,5],[8,1,13,12,20],[7,6,1,8,1],[10,16,10,11,2],[17,16,8,13,9],[12,19,11,7,4],[10,20,6,15,2],[8,15,7,13,11]]
    m = 16
    n = 5
    target = 9
    
    so = Solution()
    r = so.minCost(houses, cost, m, n, target)
    print(r)
#
# @lc app=leetcode id=1465 lang=python3
#
# [1465] Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#

# @lc code=start
class Solution:
    def maxArea(self, h: int, w: int, hc: list[int], vc: list[int]) -> int:
        hc.sort()
        hmax = 0
        for i in range(len(hc)):
            if i == 0:
                hmax = hc[0]
            else:
                hmax = max(hmax, hc[i] - hc[i-1])
        if h > hc[i]:
            hmax = max(hmax, h - hc[i])

        vc.sort()
        wmax = 0
        for i in range(len(vc)):
            if i == 0:
                wmax = vc[0]
            else:
                wmax = max(wmax, vc[i] - vc[i-1])
        if w > vc[i]:
            wmax = max(wmax, w - vc[i])

        #print(hs, ws)

        return (hmax * wmax) % 1000000007


        
# @lc code=end

h = 5
w = 4
horizontalCuts = [1,2,4]
verticalCuts = [1,3]

'''
h = 5
w = 4
horizontalCuts = [3,1]
verticalCuts = [1]

h = 5
w = 4
horizontalCuts = [3]
verticalCuts = [3]
'''

h = 6
w = 3
horizontalCuts = [5,4,1,2,3]
verticalCuts = [2,1]

so = Solution()
r = so.maxArea(h, w, horizontalCuts, verticalCuts)
print(r)
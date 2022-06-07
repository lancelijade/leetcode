#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: list[int]) -> int:
        size = len(height)
        leftmax = [0] * size
        leftmax[0] = height[0]
        rightmax = [0] * size
        rightmax[-1] = height[-1]

        for i in range(1, size):
            leftmax[i] = max(leftmax[i-1], height[i])

        for i in range(size-2, -1, -1):
            rightmax[i] = max(rightmax[i+1], height[i])

        #print(leftmax)
        #print(rightmax)

        r = 0
        for i in range(size):
            r += min(leftmax[i], rightmax[i]) - height[i]

        return r


        
# @lc code=end

height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]

so = Solution()
r = so.trap(height)
print(r)
#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        
        size = len(nums)
        if size == 1: return size

        r = 0

        s = 1
        while s < size and nums[s] == nums[0]:      # for [1,1,1,1,1]
            r += 1
            s += 1
        if s == size: return size - r

        incr, decr = False, False

        for i in range(s, size):
            if nums[i] > nums[i-1]:     # for every successive incrment, erase the first one
                if incr:
                    r += 1
                else:
                    incr = True
                    decr = False
            elif nums[i] < nums[i-1]:
                if decr:
                    r += 1
                else:
                    decr = True
                    incr = False
            else:       # erase all save value
                r += 1

        return size - r


        
# @lc code=end

nums = [1,7,4,9,2,5]
#nums = [1,1,1,2,2]
nums = [1,17,5,10,13,15,10,5,16,8]
nums = [1,2]
nums = [0,0,0]

so = Solution()
r = so.wiggleMaxLength(nums)
print(r)
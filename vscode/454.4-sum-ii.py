#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
from collections import defaultdict


class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        da = defaultdict(int)
        for a in nums1:
            for b in nums2:
                da[a+b] += 1

        db = defaultdict(int)
        for a in nums3:
            for b in nums4:
                db[a+b] += 1

        r = 0
        for k, v in da.items():
            if -k in db.keys():
                r += v * db[-k]

        return r

        
# @lc code=end

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]

nums1 = [0]
nums2 = [0]
nums3 = [0]
nums4 = [0]

so = Solution()
r = so.fourSumCount(nums1, nums2, nums3, nums4)
print(r)
class Solution:
    def twoSumLessThanK(self, nums: list[int], k: int) -> int:

        candidates = []
        ma = -1

        for num in nums:
            if num >= k:
                continue
            for can in candidates:
                m = num + can
                if m < k:
                    if m > ma:
                        ma = m
            candidates.append(num)

            #print(num, ma, candidates)

        return ma



nums = [34,23,1,24,75,33,54,8]
k = 60

nums = [10,20,30]
k = 15

so = Solution()
r = so.twoSumLessThanK(nums, k)
print(r)
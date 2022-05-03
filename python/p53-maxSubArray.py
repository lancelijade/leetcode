import pprint
pp = pprint.PrettyPrinter()


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr = ma = nums[0]
        for num in nums[1:]:
            curr = max(num, curr+num)
            ma = max(ma, curr)

        return ma


nums = [-2,1,-3,4,-1,2,1,-5,4]

so = Solution()
r = so.maxSubArray(nums)
pp.pprint(r)
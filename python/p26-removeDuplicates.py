import pprint
pp = pprint.PrettyPrinter()


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        cnt = 1
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
            j += 1
        return i + 1



nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
#nums = [1,2]

so = Solution()
r = so.removeDuplicates(nums)
pp.pprint(r)
pp.pprint(nums)
import pprint
pp = pprint.PrettyPrinter()


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == val:
                pass
            else:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i

    def removeElement2(self, nums: list[int], val: int) -> int:
        i = 0
        j = len(nums)-1
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return j+1


nums = [3,2,2,3]
val = 3
#nums = [0,1,2,2,3,0,4,2]
#val = 2
#nums = [1]
#val = 1

so = Solution()
r = so.removeElement2(nums, val)
pp.pprint(r)
pp.pprint(nums)
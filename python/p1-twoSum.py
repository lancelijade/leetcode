class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        for i in range(len(nums)-1) :
            cur = nums[i]
            to = target - cur
            j = -1
            try:
                j = nums.index(to, i+1)
            except ValueError:
                pass
            if j != -1 :
                return [i,j]

    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i in range(len(nums)):
            f = target - nums[i]
            if f in map: 
                return [map[f], i]
            map[nums[i]] = i
        

nums = [2,7,11,15]
target = 9        
#nums = [3,2,4]
#target = 6
nums = [3,3]
target = 6

so = Solution()
print(so.twoSum2(nums, target))
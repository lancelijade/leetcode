class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        p1 = 0
        a1 = 0
        p2 = 0
        ma = 0
        for n in nums:
            if n==1:
                p2 += 1
                a1 += 1
            else:
                p1 = p2
                a1 = p1+1
                p2 = 0
            ma = max(ma, a1)
        return ma


nums = [1,0,1,1,0]
nums = [1,0,1,1,0,1]

so = Solution()
r = so.findMaxConsecutiveOnes(nums)
print(r)
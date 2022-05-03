class Solution:
    def minProductSum(self, nums1: list[int], nums2: list[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)
        r = 0
        for i in range(len(nums1)):
            r += nums1[i] * nums2[i]
        return r


nums1 = [5,3,4,2]
nums2 = [4,2,2,5]
nums1 = [2,1,4,5,7]
nums2 = [3,2,4,8,6]

so = Solution()
print(so.minProductSum(nums1, nums2))
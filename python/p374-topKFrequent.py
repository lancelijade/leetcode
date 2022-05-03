from collections import Counter
import pprint
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        if k == len(nums): return nums

        c = Counter(nums)

        #return sorted(c.keys(), key=c.get, reverse=True)[:k]
        return heapq.nlargest(k, c.keys(), c.get)



nums = [1,1,1,2,2,3]
k = 2
nums = [1]
k = 1
nums = [3,0,1,0,2,2,2]
k = 1


so = Solution()
r = so.topKFrequent(nums, k)
pp = pprint.PrettyPrinter()
pp.pprint(r)
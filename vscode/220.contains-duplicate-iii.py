#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start

import bisect

class Solution2:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, t: int) -> bool:

        def find_and_insert(n):
            p = bisect.bisect(a, n)
            #print(n, p, a)
            if (p>0 and n-a[p-1]<=t) or \
                (p<len(a) and a[p]-n<=t):
                return True
            a.insert(p, n)


        a = []
        for i in range(min(k+1, len(nums))):
            r = find_and_insert(nums[i])
            if r == True: return True

        s = 0
        i = k+1
        while i < len(nums):

            a.remove(nums[s])

            r = find_and_insert(nums[i])
            if r == True: return True

            i += 1
            s += 1

        return False

        

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, t: int) -> bool:
        1


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTree:
    
    def search(self, root: TreeNode, val: int) -> TreeNode:
        
        if not root or not root.val:
            return None
        
        elif val == root.val:
            return root

        elif val < root.val:
            return self.search(root.left, val)

        else:
            return self.search(root.right, val)

        
# @lc code=end

nums = [1,5,9,1,5,9]
k = 2
t = 3
"""
nums = [1,0,1,1]
k = 1
t = 2

nums = [1,2,3,1]
k = 3
t = 0


nums = [1]
k = 1
t = 1

nums = [2147483646,2147483647]
k = 3
t = 3

nums = [8,7,15,1,6,1,9,15]
k = 1
t = 3

nums = [-3,3,-6]
k = 2
t = 3

"""
so = Solution()
r = so.containsNearbyAlmostDuplicate(nums, k, t)
print(r)
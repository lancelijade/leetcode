#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
class Solution:
    def candy(self, ratings: list[int]) -> int:
        size = len(ratings)
        l2r = [1] * size
        r2l = [1] * size

        for i in range(1, size):
            if ratings[i] > ratings[i-1]:
                l2r[i] = l2r[i-1] + 1

        for i in range(size-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                r2l[i] = r2l[i+1] + 1

        #print(l2r, r2l)

        r = 0
        for i in range(size):
            r += max(l2r[i], r2l[i])

        return r


        
# @lc code=end

ratings = [1,0,2]
ratings = [1,2,2]
ratings = [1,3,2,2,1]

so = Solution()
r = so.candy(ratings)
print(r)
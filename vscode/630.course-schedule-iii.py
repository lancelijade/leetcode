#
# @lc app=leetcode id=630 lang=python3
#
# [630] Course Schedule III
#

# @lc code=start
import heapq


class Solution:
    def scheduleCourse(self, courses):
        courses.sort(key = lambda x : x[1])
        res = []
        maxVal = 0

        for i , j in courses:
            heapq.heappush(res , -i)
            maxVal = maxVal + i
            if maxVal > j:
                temp = heapq.heappop(res)
                maxVal = maxVal + temp
        return len(res)


        
# @lc code=end

courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]


so = Solution()
r = so.scheduleCourse(courses)
print(r)
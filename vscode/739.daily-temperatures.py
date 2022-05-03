#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from collections import defaultdict, deque
from var_dump import var_dump
import pprint
pp = pprint.PrettyPrinter()
from datetime import datetime 
time_start = datetime.now()

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        r = [0] * len(temperatures)
        st = []

        for i, t in enumerate(temperatures):
            while st and t > temperatures[st[-1]]:
                j = st.pop()
                r[j] = i - j
            st.append(i)

            #print(i, t, st)

        return r

# @lc code=end

temperatures = [73,74,75,71,69,72,76,73]
temperatures = [30,40,50,60]
#temperatures = [30,60,90]

so = Solution()
r = so.dailyTemperatures(temperatures)
print(r)

time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)
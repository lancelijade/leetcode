#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two lists
#

# @lc code=start
from collections import defaultdict
import math


class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        d = defaultdict(int)

        mini = math.inf
        r = []

        for i, re in enumerate(list1):
            d[re] = i

        for i, re in enumerate(list2):
            if re in d:
                d[re] += i
                if d[re] < mini:
                    mini = d[re]
                    r = [re]
                elif d[re] == mini:
                    r.append(re)

        return r


        
# @lc code=end

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
"""
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]


list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
"""

so = Solution()
r = so.findRestaurant(list1, list2)
print(r)
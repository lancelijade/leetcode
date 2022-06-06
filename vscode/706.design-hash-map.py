#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
class MyHashMap:

    def __init__(self):
        self.h = []
        self.v = []

    def put(self, key: int, value: int) -> None:
        if key not in self.h:
            self.h.append(key)
            self.v.append(value)
        else:
            self.v[self.h.index(key)] = value


    def get(self, key: int) -> int:
        if key in self.h:
            return self.v[self.h.index(key)]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.h:
            i = self.h.index(key)
            self.h[i] = self.v[i] = None


# @lc code=end


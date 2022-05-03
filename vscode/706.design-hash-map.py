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
        k = hash(key)
        if k not in self.h:
            self.h.append(k)
            self.v.append(value)
        else:
            self.v[self.h.index(k)] = value


    def get(self, key: int) -> int:
        k = hash(key)
        if k in self.h:
            return self.v[self.h.index(k)]
        else:
            return -1

    def remove(self, key: int) -> None:
        k = hash(key)
        if k in self.h:
            i = self.h.index(k)
            self.h[i] = self.v[i] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# @lc code=end


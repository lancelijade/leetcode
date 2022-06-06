#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
from collections import defaultdict

class MyHashSet:

    def __init__(self):
        self.key = defaultdict(int)
        

    def add(self, key: int) -> None:
        self.key[key] = 1
        

    def remove(self, key: int) -> None:
        if self.contains(key):
            del self.key[key]
        

    def contains(self, key: int) -> bool:
        return key in self.key


# @lc code=end

in1 = ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
in2 = [[], [1], [2], [1], [3], [2], [2], [2], [2]]

o = None
ret = [None]
if in2[0]:
    exec('o = {}({})'.format(in1[0], in2[0][0]))
else:
    exec('o = {}()'.format(in1[0]))

for i in range(1, len(in1)):
    if (len(in2[i])>0):
        exec('ret.append(o.{}({}))'.format(in1[i], in2[i][0]))
    else:
        exec('ret.append(o.{}())'.format(in1[i]))

print(ret)
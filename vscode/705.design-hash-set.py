#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
class MyHashSet:

    N = 769

    def __init__(self):
        self.buckets = [[] for _ in range(self.N)]
        

    def add(self, key: int) -> None:
        n = key % self.N
        if key not in self.buckets[n]:
            self.buckets[n].append(key)
        

    def remove(self, key: int) -> None:
        if self.contains(key):
            n = key % self.N
            self.buckets[n].remove(key)
        

    def contains(self, key: int) -> bool:
        n = key % self.N
        return key in self.buckets[n]


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
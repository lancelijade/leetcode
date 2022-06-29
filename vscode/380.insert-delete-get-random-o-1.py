#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
from collections import defaultdict
from random import randrange


class RandomizedSet:

    def __init__(self):
        self.dict = defaultdict(int)
        self.li = []
        self.le = 0
        

    def insert(self, val: int) -> bool:
        #print("insert:", val, self.dict, self.li, self.le)
        if self.dict[val] == 0:
            n = len(self.li) + 1
            self.li.append(val)
            self.dict[val] = n
            self.le = n
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        #print("remove:", val, self.dict, self.li, self.le)
        if self.dict[val] != 0:
            pos = self.dict[val] - 1
            if pos != self.le:
                self.dict[self.li[self.le-1]] = pos + 1
                self.li[pos], self.li[self.le-1] = self.li[self.le-1], self.li[pos]
            self.li.pop()
            self.dict[val] = 0
            self.le -= 1
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        #print("random:", self.dict, self.li, self.le)
        return self.li[randrange(0, self.le)]
        


# @lc code=end

in1 = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
in2 = [[], [1], [2], [2], [], [1], [2], []]

in1 = ["RandomizedSet","insert","insert","remove","insert","remove","getRandom"]
in2 = [[],[0],[1],[0],[2],[1],[]]


from datetime import datetime 
time_start = datetime.now()


o = None
cmd = []
ret = [None]
if in2[0]:
    cmd.append('o = {}({})'.format(in1[0], in2[0][0]))
else:
    cmd.append('o = {}()'.format(in1[0]))

for i in range(1, len(in1)):
    if (len(in2[i])>0):
        cmd.append('ret.append(o.{}({}))'.format(in1[i], in2[i][0]))
    else:
        cmd.append('ret.append(o.{}())'.format(in1[i]))

for cmdd in cmd:
    print(cmdd)
    exec(cmdd)

print(ret)



time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)

from collections import defaultdict


class TwoSum:

    def __init__(self):
        self.d = defaultdict(int)
        

    def add(self, number: int) -> None:
        self.d[number] += 1
        

    def find(self, value: int) -> bool:
        for n in self.d.keys():
            r = value - n
            #print(self.d, n, r)
            if r == n:
                if self.d[r] > 1:
                    return True
            elif r in self.d:
                return True
        return False
        




from datetime import datetime 
time_start = datetime.now()


in1 = ["TwoSum", "add", "add", "add", "find", "find"]
in2 = [[], [1], [3], [5], [4], [7]]

in1 = ["TwoSum","add","find"]
in2 = [[],[0],[0]]

"""
in1 = ["TwoSum","add","add","add","find"]
in2 = [[],[3],[1],[2],[3]]

in1 = ["TwoSum","add","add","add","find"]
in2 = [[],[0],[-1],[1],[0]]
"""

o = None
cmd = []
ret = [None]
if in2[0]:
    cmd.append('o = {}()'.format(in1[0]))
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

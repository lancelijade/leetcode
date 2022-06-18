class Logger:

    def __init__(self):
        self.d = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.d:
            if timestamp - self.d[message] >= 10:
                self.d[message] = timestamp
                return True
            else:
                return False

        else:
            self.d[message] = timestamp
            return True




in1 = ["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
in2 = [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]

o = None
cmd = []
ret = []
if in2[0]:
    cmd.append('o = {}({})'.format(in1[0], in2[0][0]))
else:
    cmd.append('o = {}()'.format(in1[0]))

for i in range(1, len(in1)):
    if (len(in2[i])>0):
        cmd.append('ret.append(o.{}({}, "{}"))'.format(in1[i], in2[i][0], in2[i][1]))
    else:
        cmd.append('ret.append(o.{}())'.format(in1[i]))

for cmdd in cmd:
    print(cmdd)
    exec(cmdd)

print(ret)
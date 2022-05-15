from datetime import datetime 
time_start = datetime.now()



in1 = ["MyQueue", "push", "push", "peek", "pop", "empty"]
in2 = [[], [1], [2], [], [], []]

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



time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)


class Solution:
    1

def log(func):
    def wrapper(*args, **kw):
        from datetime import datetime 
        time_start = datetime.now()
        #print('call %s():' % func.__name__)
        r = func(*args, **kw)
        time_end = datetime.now()
        print("---\ntime cost:",time_end-time_start)
        return r
    return wrapper

@log
def run():
    so = Solution()
    r = so.fib()
    print(r)

run()
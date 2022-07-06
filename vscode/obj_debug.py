if __name__ == "__main__":
    
    from var_dump import var_dump
    from datetime import datetime 
    time_start = datetime.now()

    in1 = ["MyQueue", "push", "push", "peek", "pop", "empty"]
    in2 = [[], [1], [2], [], [], []]

    o = None
    cmd = []
    ret = [None]
    if in2[0]:
        cmd.append('o = {}({})'.format(in1[0], in2[0][0]))
    else:
        cmd.append('o = {}()'.format(in1[0]))

    for i in range(1, len(in1)):
        if len(in2[i])>0:
            msg = ",".join(map(str, in2[i]))
            cmd.append('ret.append(o.{}({}))'.format(in1[i], msg))
        else:
            cmd.append('ret.append(o.{}())'.format(in1[i]))

    for cmdd in cmd:
        print(cmdd)
        exec(cmdd)
        var_dump(o)
        print("=====\n")

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
def run(*args, **kw):
    so = Solution()
    r = so.numDistinctIslands(*args, **kw)
    print(r)

grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
#grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
run(grid)
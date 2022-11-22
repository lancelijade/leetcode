class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        p = 0
        q = len(num) - 1

        while p < q:
            #print(p, q)
            if num[p] in ['0', '1', '8'] and num[q] == num[p]:
                1
            elif num[p] == '6' and num[q] == '9':
                1              
            elif num[p] == '9' and num[q] == '6':
                1
            else:
                return False
            p += 1
            q -= 1

        if p == q:
            if num[p] not in ['0', '1', '8']:
                return False

        return True
        


if __name__ == "__main__":

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
        r = so.isStrobogrammatic(*args, **kw)
        print(r)


    num = "8"

    run(num)


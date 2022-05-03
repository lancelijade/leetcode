class Solution:
    def findPermutation(self, s: str) -> list[int]:

        s += 'I'
        pos = 0
        dstart = None
        r = []

        while pos<len(s):
            if s[pos] == 'D':
                if dstart is None:      # I->D
                    dstart = pos
                else:                   # D->D
                    pass
            else:
                if dstart is None:      # I->I
                    r.append(pos+1)
                else:                   # D->I
                    r += list(range(pos+1, dstart, -1))
                    dstart = None
            pos += 1

        return r
        

s = "I"
s = "DI"
#s = "DD"

so = Solution()
r = so.findPermutation(s)
print(r)
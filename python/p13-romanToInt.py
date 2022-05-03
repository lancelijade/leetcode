import pprint

class Solution:
    def romanToInt(self, s: str) -> int:
        
        d = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

        r = 0
        i = 0
        le = len(s)
        while i < le:
            if i < le-1 and d[s[i]] < d[s[i+1]]:
                r += d[s[i+1]] - d[s[i]]
                i += 2

            else:
                r += d[s[i]]
                i += 1
        
        return r


s = "MCMXCIV"
#s = "LVIII"

so = Solution()
r = so.romanToInt(s)
pp = pprint.PrettyPrinter()
pp.pprint(r)
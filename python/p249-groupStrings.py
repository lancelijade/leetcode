from collections import defaultdict


class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        
        def shift(s):
            r = []
            diff = ord('z') - ord(s[0]) 
            print(diff)
            if diff:
                for c in s:
                    r.append(chr((ord(c) + diff - ord('a')) % 26 + ord('a')))
                    #print(c, r)
                return "".join(r)
            else:
                return s

        d = defaultdict(list[str])
        for s in strings:
            d[shift(s)].append(s)

        #print(d)
        return d.values()



strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

so = Solution()
r = so.groupStrings(strings)
print(r)
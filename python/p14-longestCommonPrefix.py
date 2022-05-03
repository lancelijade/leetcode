import pprint
pp = pprint.PrettyPrinter()

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        if len(strs) == 1: return strs[0]

        le = len(strs[0])
        comm = strs[0]
        #pp.pprint(le)
        #pp.pprint(comm)

        for j in range(len(strs))[1:]:
            i = 0
            while i < min(len(strs[j]), le):
                if strs[j][i] == comm[i]: 
                    i += 1
                else:
                    break
            nle = i
            if nle == 0: return ""
            if nle < le: 
                comm = comm[:nle]
                le = nle
            #pp.pprint(le)
            #pp.pprint(comm)

        return comm


strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]
strs = ["aba","ab","aaca","aca"]
#strs = ["flower","flower","flower","flower"]



so = Solution()
r = so.longestCommonPrefix(strs)
pp.pprint(r)
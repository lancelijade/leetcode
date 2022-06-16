#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
from functools import cache


class Solution:
    def longestPalindrome2(self, s: str) -> str:
        
        @cache
        def lcs(s1, s2, i, j):
            #print(s1, s2, i, j )
            if i == 0 or j == 0:
                return ''
            elif s1[i-1] == s2[j-1]:
                return lcs(s1, s2, i-1, j-1) + s1[i-1]
            else:
                r1 = lcs(s1, s2, i-1, j)
                r2 = lcs(s1, s2, i, j-1)
                if len(r1) > len(r2):
                    return r1
                else:
                    return r2

        s2 = "".join(list(reversed(s)))
        return lcs(s, s2, len(s), len(s))


    def longestPalindrome(self, s: str) -> str:
        
        def expand(i, j):
            if i-1>=0 and j+1<len(s) and s[i-1] == s[j+1]:
                return expand(i-1, j+1)
            else:
                return i, j
        
        maxlen = 0
        mi, mj = 0, 0
        for i in range(len(s)-1):
            if i * 2 >= maxlen:
                ri, rj = expand(i, i)
                if rj - ri + 1 > maxlen:
                    maxlen = rj - ri + 1
                    mi, mj = ri, rj

                if s[i] == s[i+1]:
                    ri, rj = expand(i, i+1)
                    if rj - ri + 1 > maxlen:
                        maxlen = rj - ri + 1
                        mi, mj = ri, rj

        return s[mi:mj+1]

        


        
# @lc code=end

s = "babad"
s = "bb"
#s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#s = "glwhcebdjbdroiurzfxxrbhzibilmcfasshhtyngwrsnbdpzgjphujzuawbebyhvxfhtoozcitaqibvvowyluvdbvoqikgojxcefzpdgahujuxpiclrrmalncdrotsgkpnfyujgvmhydrzdpiudkfchtklsaprptkzhwxsgafsvkahkbsighlyhjvbburdfjdfvjbaiivqxdqwivsjzztzkzygcsyxlvvwlckbsmvwjvrhvqfewjxgefeowfhrcturolvfgxilqdqvitbcebuooclugypurlsbdfquzsqngbscqwlrdpxeahricvtfqpnrfwbyjvahrtosovsbzhxtutyfjwjbpkfujeoueykmbcjtluuxvmffwgqjgrtsxtdimsescgahnudmsmyfijtfrcbkibbypenxnpiozzrnljazjgrftitldcueswqitrcvjzvlhionutppppzxoepvtzhkzjetpfqsuirdcyqfjsqhdewswldawhdyijhpqtrwgyfmmyhhkrafisicstqxokdmynnnqxaekzcgygsuzfiguujyxowqdfylesbzhnpznayzlinerzdqjrylyfzndgqokovabhzuskwozuxcsmyclvfwkbimhkdmjacesnvorrrvdwcgfewchbsyzrkktsjxgyybgwbvktvxyurufsrdufcunnfswqddukqrxyrueienhccpeuqbkbumlpxnudmwqdkzvsqsozkifpznwapxaxdclxjxuciyulsbxvwdoiolgxkhlrytiwrpvtjdwsssahupoyyjveedgqsthefdyxvjweaimadykubntfqcpbjyqbtnunuxzyytxfedrycsdhkfymaykeubowvkszzwmbbjezrphqildkmllskfawmcohdqalgccffxursvbyikjoglnillapcbcjuhaxukfhalcslemluvornmijbeawxzokgnlzugxkshrpojrwaasgfmjvkghpdyxt"

so = Solution()
r = so.longestPalindrome(s)
print(r)
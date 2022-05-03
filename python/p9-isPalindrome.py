from var_dump import var_dump

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        s = 0
        e = len(x)-1
        while s < e:
            if x[s] != x[e]: return False
            s += 1
            e -= 1
        return True


x = -121

so = Solution()
r = so.isPalindrome(x)
var_dump(r)

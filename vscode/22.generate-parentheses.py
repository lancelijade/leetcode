#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from collections import deque


class Solution:
    def generateParenthesis2(self, n: int, s = "", n2 = 0) -> list[str]:
        #print(n, s, n2)
        if n == 0:
            if n2 == 0:
                return [s]
            else:
                return [s + ')' * n2]

        r = []
        r += self.generateParenthesis(n-1, s + '(', n2+1)
        if n2 > 0:
            r += self.generateParenthesis(n, s + ')', n2-1)
        return r


    def generateParenthesis(self, n: int) -> list[str]:
        r = []
        q = deque([(n-1, 1, '(')])

        while q:
            #print(q)
            n, n2, s = q.popleft()

            if n == 0:
                if n2 == 0:
                    r += [s]
                else:
                    r += [s + ')' * n2]
                    n2 = 0

            if n > 0:
                q.append((n-1, n2+1, s + '('))
            if n2 > 0:
                q.append((n, n2-1, s + ')'))

        return r

        
# @lc code=end

n = 3
n = 1

so = Solution()
r = so.generateParenthesis(n)
print(r)
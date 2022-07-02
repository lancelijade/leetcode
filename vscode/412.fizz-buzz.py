#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        r = [str(i+1) for i in range(n)]
        for i in range(3, n+1, 3):
            r[i-1] = "Fizz"
        for i in range(5, n+1, 5):
            r[i-1] = "Buzz"
        for i in range(15, n+1, 15):
            r[i-1] = "FizzBuzz"

        return r

        
# @lc code=end

n = 15

so = Solution()
r = so.fizzBuzz(n)
print(r)
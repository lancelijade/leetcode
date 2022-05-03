import pprint
pp = pprint.PrettyPrinter()


class Solution:
    def calPoints(self, ops: list[str]) -> int:

        dp = {}
        dp[0] = int(ops[0])
        i = 1
        j = 1

        while i < len(ops):
            match ops[i]:
                case "C":
                    dp[j-1] = 0
                    j -= 1
                case "D":
                    dp[j] = dp[j-1] * 2
                    j += 1
                case "+":
                    dp[j] = dp[j-2] + dp[j-1]
                    j += 1
                case _:
                    dp[j] = int(ops[i])
                    j += 1
            i += 1
        
        #pp.pprint(dp)
        return sum(dp.values())
        

    def calPoints2(self, ops: list[str]) -> int:
        stack = []
        for op in ops:
            if op == "+":
                stack.append(stack[-2] + stack[-1])
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)


ops = ["5","2","C","D","+"]
ops = ["5","-2","4","C","D","9","+","+"]

so = Solution()
r = so.calPoints(ops)
pp.pprint(r)

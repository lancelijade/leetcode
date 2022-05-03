#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#



# @lc code=start
from collections import deque


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ev = deque()
        for token in tokens:
            match token:
                case "+":
                    op1 = ev.pop()
                    op2 = ev.pop()
                    val = op1 + op2
                    ev.append(val)
                case "-":
                    op1 = ev.pop()
                    op2 = ev.pop()
                    val = op2 - op1
                    ev.append(val)
                case "*":
                    op1 = ev.pop()
                    op2 = ev.pop()
                    val = op1 * op2
                    ev.append(val)
                case "/":
                    op1 = ev.pop()
                    op2 = ev.pop()
                    val = int(op2 / op1)
                    ev.append(val)
                case _:
                    ev.append(int(token))

        return ev[0]

        
# @lc code=end

tokens = ["2","1","+","3","*"]
tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

so = Solution()
r = so.evalRPN(tokens)
print(r)
import pprint
pp = pprint.PrettyPrinter()

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        
        q = deque()

        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                q.append(s[i])
            else:
                if len(q) == 0: return False
                
                c = q.pop()
                if (c=='(' and s[i]==')') or (c=='[' and s[i]==']') or (c=='{' and s[i]=='}'): 
                    pass
                else:
                    return False

        return len(q) == 0


s = "(()[]{}"


so = Solution()
r = so.isValid(s)
pp.pprint(r)
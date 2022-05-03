import pprint
pp = pprint.PrettyPrinter()


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rsplit(maxsplit=2)[-1])


s = "   fly me   to   the moon  "
#s = "Hello World"
#s = "luffy is still joyboy"

so = Solution()
r = so.lengthOfLastWord(s)
pp.pprint(r)
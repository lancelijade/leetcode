import pprint
pp = pprint.PrettyPrinter()


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


haystack = "hello"
needle = "ll"
haystack = "aaaaa"
needle = ""

so = Solution()
r = so.strStr(haystack, needle)
pp.pprint(r)
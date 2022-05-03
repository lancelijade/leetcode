import pprint
pp = pprint.PrettyPrinter()


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        for d in range(len(digits)-1, -1, -1):
            carry, digits[d] = divmod(digits[d]+1, 10)
            if carry == 0: break

        if carry: digits.insert(0, 1)
        return digits
        


digits = [9, 9]
#digits = [4,3,2,1]

so = Solution()
r = so.plusOne(digits)
pp.pprint(r)
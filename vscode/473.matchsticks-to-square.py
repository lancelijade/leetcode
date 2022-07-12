#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#

# @lc code=start
class Solution:
    def makesquare2(self, matchsticks: list[int]) -> bool:

        def dfs(i):
            #print(i, sums)
            if i == size-1:
                return sums[0] == sums[1] == sums[2] == le

            for j in range(4):
                if sums[j] + matchsticks[i] <= le:
                    sums[j] += matchsticks[i]
                    if dfs(i+1): return True
                    sums[j] -= matchsticks[i]

            return False


        su = sum(matchsticks)
        if su % 4 != 0: return False

        le = su // 4
        if max(matchsticks) > le:
            return False

        size = len(matchsticks)
        sums = [0] * 4
        matchsticks.sort(reverse=True)

        return dfs(0)


    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # If there are no matchsticks, then we can't form any square.
        if not nums:
            return False

        # Number of matchsticks
        L = len(nums)

        # Possible perimeter of our square
        perimeter = sum(nums)

        # Possible side of our square from the given matchsticks
        possible_side =  perimeter // 4

        # If the perimeter isn't equally divisible among 4 sides, return False.
        if possible_side * 4 != perimeter:
            return False

        # Memoization cache for the dynamic programming solution.
        memo = {}

        # mask and the sides_done define the state of our recursion.
        def recurse(mask, sides_done):

            # This will calculate the total sum of matchsticks used till now using the bits of the mask.
            total = 0
            for i in range(L - 1, -1, -1):
                if not (mask & (1 << i)):
                    total += nums[L - 1 - i]

            # If some of the matchsticks have been used and the sum is divisible by our square's side, then we increment the number of sides completed.
            if total > 0 and total % possible_side == 0:
                sides_done += 1

            # If we were successfully able to form 3 sides, return True
            if sides_done == 3:
                return True

            # If this recursion state has already been calculated, just return the stored value.
            if (mask, sides_done) in memo:
                return memo[(mask, sides_done)]

            # Common variable to store answer from all possible further recursions from this step.
            ans = False

            # rem stores available space in the current side (incomplete).
            c = int(total / possible_side)
            rem = possible_side * (c + 1) - total

            # Iterate over all the matchsticks
            for i in range(L - 1, -1, -1):

                # If the current one can fit in the remaining space of the side and it hasn't already been taken, then try it out
                if nums[L - 1 - i] <= rem and mask&(1 << i):

                    # If the recursion after considering this matchstick gives a True result, just break. No need to look any further.
                    # mask ^ (1 << i) makes the i^th from the right, 0 making it unavailable in future recursions.
                    if recurse(mask ^ (1 << i), sides_done):
                        ans = True
                        break
            # cache the result for the current recursion state.            
            memo[(mask, sides_done)] = ans
            return ans

        # recurse with the initial mask with all matchsticks available.
        return recurse((1 << L) - 1, 0)


# @lc code=end

if __name__ == "__main__":

    from var_dump import var_dump
    from datetime import datetime 
    time_start = datetime.now()


    matchsticks = [1,1,2,2,2]
    #matchsticks = [3,3,3,3,4]
    #matchsticks = [1,2,2,3,4,4]
    matchsticks = [5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511]
    matchsticks = [14,10,10,10,10,10,10,10,10,10,10,10,8,9,19]


    so = Solution()
    r = so.makesquare(matchsticks)
    print(r)

    time_end = datetime.now()
    print("---\ntime cost:",time_end-time_start)
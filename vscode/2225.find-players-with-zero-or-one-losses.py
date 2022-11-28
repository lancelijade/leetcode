#
# @lc app=leetcode id=2225 lang=python3
#
# [2225] Find Players With Zero or One Losses
#

# @lc code=start
class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        
        winner = set()
        winner2 = set()
        loser = set()

        for ma in matches:
            if ma[0] not in winner2 and ma[0] not in loser:
                winner.add(ma[0])
            
            if ma[1] in winner:
                winner.remove(ma[1])
                winner2.add(ma[1])
            elif ma[1] in winner2:
                winner2.remove(ma[1])
                loser.add(ma[1])
            elif ma[1] not in loser:
                winner2.add(ma[1])

        return [sorted(winner), sorted(winner2)]

        
# @lc code=end

if __name__ == "__main__":
    
    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    matches = [[2,3],[1,3],[5,4],[6,4]]
    
    so = Solution()
    r = so.findWinners(matches)
    print(r)
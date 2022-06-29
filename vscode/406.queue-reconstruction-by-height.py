#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#

# @lc code=start
class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        ps = sorted(people, reverse = True)
        #print(ps)

        q = []
        while len(ps)>0:

            h0 = ps[0][0]
            end = 1
            for i in range(1, len(ps)):
                if ps[i][0] != h0:
                    end = i
                    break
                end = i+1
            
            #print(ps[0:end])

            for p in reversed(ps[0:end]):
                q.insert(p[1], p)
            #print(q)

            ps = ps[end:]
            #print(ps)

        return q


        
# @lc code=end

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
people = [[8,2],[4,2],[4,5],[2,0],[7,2],[1,4],[9,1],[3,1],[9,0],[1,0]]

so = Solution()
r = so.reconstructQueue(people)
print(r)
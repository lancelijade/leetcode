#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#

# @lc code=start
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        ma = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ma[j][i] = matrix[i][j]
        return ma

        
# @lc code=end

matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3],[4,5,6]]

so = Solution()
r = so.transpose(matrix)
print(r)
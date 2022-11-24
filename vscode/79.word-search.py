#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        wlen = len(word)
        dirs = ((0,1),(1,0),(0,-1),(-1,0))
        visited = set()

        def dfs(x, y, pos):
            #print(x, y, pos, visited)
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and (nx, ny) not in visited and board[nx][ny] == word[pos]:
                    if pos == wlen - 1:
                        return True
                    visited.add((nx, ny))
                    r = dfs(nx, ny, pos+1)
                    #print(nx, ny, pos+1, r)
                    if r: return r
                    visited.remove((nx, ny))
            return False
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if wlen == 1: 
                        return True
                    visited.add((i, j))
                    r = dfs(i, j, 1)
                    if r: return r
                    visited.remove((i, j))

        return False

        
# @lc code=end

if __name__ == "__main__":
    
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"

    #board = [["A","B","C","E"], ["S","F","C","S"], ["A","D","E","E"]]
    #word = "ABCB"
    
    board = [["a"]]
    word = "a"


    so = Solution()
    r = so.exist(board, word)
    print(r)
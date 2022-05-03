import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        
        def dfs(node: int):
            if node == n-1:
                r.append(path.copy())
                return

            for i in graph[node]:
                path.append(i)
                dfs(i)
                path.pop()


        n = len(graph)
        r = []
        path = [0]
        dfs(0)
        return r


graph = [[1,2],[3],[3],[]]
graph = [[4,3,1],[3,2,4],[3],[4],[]]

so = Solution()
r = so.allPathsSourceTarget(graph)
pp.pprint(r)
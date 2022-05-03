import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def buildGraph(adjList: list[list[int]]) -> Node:

    n = len(adjList)
    if not n: return None

    graph = {}
    
    i = 1
    while i <= n:
        graph[i] = Node(i)
        i += 1

    i = 1
    for a in adjList:
        for j in a:
            graph[i].neighbors.append(graph[j])
        i += 1

    return graph[1]


class Solution:

    def __init__(self):
        self.nodeList = {}

    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node: return None

        if node in self.nodeList: return self.nodeList[node]
                
        self.nodeList[node] = Node(node.val)
        for nb in node.neighbors:
            self.nodeList[node].neighbors.append(self.cloneGraph(nb))

        return self.nodeList[node]


adjList = [[2,4],[1,3],[2,4],[1,3]]
#adjList = [[]]
#adjList = []

head = buildGraph(adjList)

so = Solution()
r = so.cloneGraph(head)
pp.pprint(r)
#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from collections import deque


class Solution:
    def isBipartite2(self, graph: list[list[int]]) -> bool:
        
        q = range(len(graph))
        q = deque(q)
        parties = (set(),set())

        q2 = deque()

        while q:
            i = q.popleft()
            if not graph[i]: continue
            if not parties[0] and not parties[1]:
                parties[0].add(i)

            for j in graph[i]:
                #print(i,j)
                if (i in parties[0] and j in parties[0]) or (i in parties[1] and j in parties[1]):
                    return False
                    
                if i in parties[0]:
                    parties[1].add(j)
                elif j in parties[0]:
                    parties[1].add(i)
                elif i in parties[1]:
                    parties[0].add(j)
                elif j in parties[1]:
                    parties[0].add(i)
                else:
                    if i not in q2:q2.append(i)
                    if j not in q2:q2.append(j)

                #print(parties)
                #print(q)
                #print(q2)

        while q2:
            i = q2.popleft()
            if i not in parties[0] and i not in parties[1]:
                parties[0].add(i)

            for j in graph[i]:
                #print(i,j)
                if (i in parties[0] and j in parties[0]) or (i in parties[1] and j in parties[1]):
                    return False
                    
                if i in parties[0]:
                    parties[1].add(j)
                elif j in parties[0]:
                    parties[1].add(i)
                elif i in parties[1]:
                    parties[0].add(j)
                elif j in parties[1]:
                    parties[0].add(i)
                else:
                    if i not in q2:q2.append(i)
                    if j not in q2:q2.append(j)

                #print(parties)
                #print(q2)        

        return True


    def isBipartite(self, graph: list[list[int]]) -> bool:
        st = []
        color = [-1] * len(graph)

        while -1 in color or st:
            if not st:
                st.append((color.index(-1), 0))

            i, co = st.pop()
            #print(i, co)
            color[i] = co
            for j in graph[i]:
                if color[j] == co: 
                    return False
                elif color[j] != -1:
                    continue
                color[j] = abs(co-1)#
                if (j, color[j]) not in st:
                    st.append((j, color[j]))

            #print(st)
            #print(color)

        return True
        
# @lc code=end

graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
#graph = [[1,3],[0,2],[1,3],[0,2]]
graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
graph = [[],[10,44,62],[98],[59],[90],[],[31,59],[52,58],[],[53],[1,63],[51,71],[18,64],[24,26,45,95],[61,67,96],[],[40],[39,74,79],[12,21,72],[35,85],[86,88],[18,76],[71,80],[27,58,85],[13,26,87],[75,94],[13,24,68,77,82],[23],[56,96],[67],[56,73],[6],[41],[50,88,91,94],[],[19,72,92],[59],[49],[49,89],[17],[16],[32,84,86],[61,73,77],[94,98],[1,74],[13,57,90],[],[93],[],[37,38,54,68],[33],[11],[7,85],[9],[49],[61],[28,30,87,93],[45,69,77],[7,23,76],[3,6,36,62],[81],[14,42,55,62],[1,59,61],[10],[12,93],[],[96],[14,29,70,73],[26,49,71,76],[57,83],[67],[11,22,68,89],[18,35],[30,42,67],[17,44],[25],[21,58,68],[26,42,57,95],[],[17],[22,83],[60],[26,83,84,94],[69,80,82],[41,82],[19,23,52],[20,41],[24,56],[20,33],[38,71,99],[4,45],[33],[35],[47,56,64],[25,33,43,82],[13,77],[14,28,66],[],[2,43],[89]]
graph = [[1,4],[0,2],[1],[4],[0,3]]
graph = [[1],[0],[4],[4],[2,3]]


so = Solution()
r = so.isBipartite(graph)
print(r)
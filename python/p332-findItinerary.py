import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump
from sortedcontainers import SortedList

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        
        def dfs(city, path):

            pp.pprint(city)
            pp.pprint(path)

            for i, t in enumerate(tickets):

                if i in used: continue

                src, tgt = t

                if src == city:

                    path.append(tgt)

                    if len(used) == triplen-1:
                        return path
                    else:
                        used.append(i)
                        r = dfs(tgt, path)
                        if r: return r
                        used.pop()

                    path.pop()

            return False

        tickets.sort()
        used = []
        triplen = len(tickets)
        #pp.pprint(tickets)
        return dfs("JFK", ["JFK"])


class Solution2:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        
        def dfs(city, path):

            #pp.pprint(city)
            #pp.pprint(path)

            if city not in tMap: return False

            for tgt in tMap[city]:

                path.append(tgt)

                if len(path) == triplen+1:
                    return path
                else:
                    tMap[city].remove(tgt)
                    r = dfs(tgt, path)
                    if r: return r
                    tMap[city].add(tgt)

                path.pop()

            return False

        tMap = {}
        for src, tgt in tickets:
            if src not in tMap:
                tMap[src] = SortedList()
            tMap[src].add(tgt)

        #var_dump(tMap)
        triplen = len(tickets)
        return dfs("JFK", ["JFK"])



tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
#tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]


so = Solution2()
r = so.findItinerary(tickets)
pp.pprint(r)
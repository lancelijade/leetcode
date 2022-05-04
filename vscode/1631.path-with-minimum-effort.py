#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

import pprint
from executing import Source
pp = pprint.PrettyPrinter()
from var_dump import var_dump
from collections import defaultdict
import math
import heapq
from collections import deque
from datetime import datetime 
time_start = datetime.now()

# @lc code=start
class Solution2:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:

        m = len(heights)
        n = len(heights[0])
        if m*n==1: return 0

        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        adjList = defaultdict(dict)
        for i in range(m):
            for j in range(n):
                pos = i * n + j
                for dx, dy in dirs:
                    nx = i+dx
                    ny = j+dy
                    npos = nx * n + ny
                    if nx>=0 and ny>=0 and nx<m and ny<n:
                        wt = abs(heights[nx][ny] - heights[i][j])
                        adjList[pos][npos] = wt
                        adjList[npos][pos] = wt
        #pp.pprint(adjList)

        r = defaultdict(dict)
        r[0] = [math.inf for _ in range(n*m)]
        r[0][0] = 0
        arr = set(adjList[0].keys())
        #pp.pprint(r)
        #pp.pprint(arr)

        i = 1
        while i < m*n:
            r[i] = r[i-1].copy()
            modi = False
            arr1 = set()
            for j in arr:
                for k, v in adjList[j].items():
                    t = r[i][j]
                    r[i][j] = min(max(r[i-1][k],v), r[i][j])
                    if t != r[i][j]: 
                        modi = True
                        #print("ijk", i,j,k)
                        arr1 = arr1.union(adjList[j].keys())
            arr = arr1.copy()
            #pp.pprint(arr)
            i += 1
            if not modi: break

        return r[i-1][-1]


class Solution3:        # dj's
    def minimumEffortPath(self, heights: list[list[int]]) -> int:

        m = len(heights)
        n = len(heights[0])
        if m*n==1: return 0

        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        adjList = defaultdict(dict)
        for i in range(m):
            for j in range(n):
                pos = i * n + j
                for dx, dy in dirs:
                    nx = i+dx
                    ny = j+dy
                    npos = nx * n + ny
                    if nx>=0 and ny>=0 and nx<m and ny<n:
                        wt = abs(heights[nx][ny] - heights[i][j])
                        adjList[pos][npos] = wt
                        adjList[npos][pos] = wt
        #pp.pprint(adjList)

        q = []
        visited = set()
        visited.add(0)
        ef = [math.inf for _ in range(n*m)]
        ef[0] = 0
        for tgt, va in adjList[0].items():
            heapq.heappush(q, (va, tgt, 0))
        #pp.pprint(ef)
        #pp.pprint(q)

        while q:
            va, src, efsofar = heapq.heappop(q)
            #print("va-src", va, src)
            if src == m*n-1: return max(efsofar, va)

            if src in visited: continue
            visited.add(src)

            ef[src] = max(efsofar, va)
            for tgt, va in adjList[src].items():
                if tgt not in visited: heapq.heappush(q, (va, tgt, ef[src]))

            #pp.pprint(visited)
            #print("ef=", ef)
            #print("q=", q)        

class UnionFind:
    def __init__(self, size: int) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x: int) -> int:
        if x == self.root[x]: return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]        

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y) -> int:
        return self.find(x) == self.find(y)


class Solution:        # uf
    def minimumEffortPath(self, heights: list[list[int]]) -> int:

        m = len(heights)
        n = len(heights[0])
        if m*n==1: return 0

        pq = []
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(m):
            for j in range(n):
                pos = i * n + j
                for dx, dy in dirs:
                    nx = i+dx
                    ny = j+dy
                    npos = nx * n + ny
                    if nx>=0 and ny>=0 and nx<m and ny<n:
                        wt = abs(heights[nx][ny] - heights[i][j])
                        heapq.heappush(pq, (wt, pos, npos))

        uf = UnionFind(m*n)
        while pq:
            wt, pos, tgt = heapq.heappop(pq)
            #print(wt, pos, tgt)

            uf.union(pos, tgt)
            if uf.connected(0, m*n-1):
                return wt

            #print(pq)
            #var_dump(uf)


# @lc code=end

heights = [[1,2,2],[3,8,2],[5,3,5]]
heights = [[1,2,3],[3,8,4],[5,3,5]]
heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
#heights = [[1,10,6,7,9,10,4,9]]
#heights = [[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]]
#heights = [[3]]
heights = [[393,518,370,274,275,248,66,322,373,820,904,986,896,292,894,368,27,412,204,109,752,473,492,113,661,849,613],[778,877,319,249,290,954,632,336,819,142,420,39,353,134,157,592,410,255,64,363,586,672,342,497,8,628,283],[758,425,342,9,290,607,890,882,480,705,400,942,516,127,869,46,653,314,625,680,256,610,305,515,556,424,690],[191,698,370,523,508,585,564,924,577,631,607,738,177,218,749,811,105,69,295,256,966,275,837,764,629,790,343],[726,669,664,273,106,171,802,353,378,21,343,34,663,651,793,23,19,603,658,282,635,314,461,643,834,415,589],[728,209,202,984,828,798,873,500,90,197,72,781,227,253,134,690,931,359,389,54,331,971,67,389,60,754,963],[869,1000,832,801,471,207,995,713,875,508,998,916,186,637,79,62,915,399,743,165,639,19,968,59,591,834,136],[831,180,765,114,411,524,361,295,4,343,686,484,305,962,714,803,597,727,317,886,936,256,249,202,334,820,560],[741,34,381,953,283,810,715,811,34,931,731,726,115,539,844,300,141,764,198,866,811,583,269,457,20,345,421],[701,770,289,571,822,292,899,825,603,920,740,474,641,620,1,292,943,994,323,710,335,49,882,970,822,984,396],[794,827,255,29,599,593,299,865,433,813,990,266,710,47,503,158,745,532,288,490,304,611,357,617,39,493,587],[806,110,818,571,254,821,309,724,137,933,175,754,251,409,921,69,90,582,479,771,715,487,689,393,449,796,185],[521,637,523,280,479,620,356,861,662,234,222,454,416,722,753,963,834,630,524,27,241,405,818,302,373,416,847],[390,304,665,253,299,714,881,24,876,623,363,55,31,840,940,781,6,636,54,545,219,148,767,295,852,957,13],[366,675,322,120,676,897,318,906,249,336,530,915,590,633,389,587,933,582,990,382,420,395,662,349,157,19,664],[177,66,802,644,216,525,797,434,701,299,352,186,733,152,280,415,205,813,692,227,136,423,616,325,314,549,788],[587,570,578,384,129,136,249,902,540,472,41,13,12,439,841,835,550,730,948,984,622,708,184,877,650,891,803],[885,986,323,340,987,557,145,253,933,22,513,216,230,632,289,659,624,441,214,311,205,96,609,55,483,22,820],[997,963,858,442,20,51,12,551,635,667,583,720,973,788,404,737,929,30,641,880,433,919,204,544,258,542,859],[659,575,369,692,909,840,721,697,890,478,778,521,802,740,240,106,818,266,559,693,152,307,821,119,979,40,894],[151,797,897,140,328,289,210,231,405,390,941,340,790,784,330,282,641,128,260,501,282,512,180,338,248,823,587],[108,840,513,238,616,892,299,664,774,420,946,115,99,755,255,1000,776,850,338,22,286,254,36,724,983,882,21],[458,511,318,455,424,899,362,885,206,429,38,810,407,815,960,812,224,906,793,973,565,285,401,660,484,68,662],[732,423,652,884,285,88,974,278,284,486,393,900,797,16,963,360,382,211,91,493,649,773,529,964,323,356,619],[952,370,1,308,509,133,195,183,231,295,512,219,781,368,625,817,727,422,723,386,96,570,262,24,6,881,357],[642,294,714,668,157,894,960,861,210,5,861,10,803,15,552,541,548,988,984,866,534,722,243,675,574,315,152],[892,785,641,994,805,783,180,672,301,947,434,316,111,242,267,723,266,792,746,600,581,367,666,977,585,852,782],[426,172,921,424,141,629,564,750,123,615,936,531,36,908,567,796,954,241,22,963,762,134,503,305,70,840,813],[519,212,933,985,901,556,41,390,308,796,819,199,406,347,41,357,417,108,263,212,923,355,783,723,459,765,641],[458,110,290,236,686,386,319,733,961,621,566,312,526,678,729,547,164,497,301,37,5,287,789,607,960,897,312],[202,987,186,987,200,34,438,395,877,231,267,384,900,894,311,790,709,670,338,540,800,913,630,634,836,278,299],[264,276,692,874,636,765,86,424,180,361,664,564,53,591,922,25,101,294,642,333,287,32,870,459,820,84,191],[168,517,515,139,677,228,637,805,915,285,859,578,999,88,212,632,573,537,89,112,526,423,515,496,631,20,209],[106,375,456,689,471,805,476,544,733,362,162,713,503,227,833,695,6,257,241,540,946,118,204,434,277,92,3],[610,151,90,370,981,63,821,231,770,722,793,867,204,637,561,947,643,758,423,489,504,276,362,752,388,182,909],[359,10,765,978,827,250,822,999,764,688,459,377,340,635,202,481,23,20,136,587,755,491,880,884,657,91,989],[320,916,632,764,737,675,115,494,793,637,313,226,824,399,900,450,281,1,631,293,871,431,811,774,192,358,114],[165,374,970,511,520,110,262,724,801,829,858,531,867,882,799,306,92,389,319,93,728,13,347,469,240,575,604]]
#heights = [[869,55,270,479,856,956,31,202,120,625,971,800,954,726,184,566,484,578,572,870,91,10,692,403,7,719,818,522,481,221,187,120,140,14],[495,203,126,556,580,247,570,874,563,789,888,186,971,470,509,742,587,728,240,189,883,704,671,116,163,462,110,686,137,674,903,590,216,445],[948,976,555,959,172,823,66,641,816,622,913,24,692,112,222,276,509,407,770,211,878,390,104,610,88,67,771,916,141,412,744,479,642,575],[323,297,620,203,42,182,31,338,653,554,539,792,895,491,713,423,4,592,459,194,502,689,244,39,608,184,705,971,688,677,284,135,850,191],[379,123,172,96,618,96,980,760,89,800,786,904,734,90,795,776,844,732,871,90,158,724,384,261,697,802,740,946,113,725,547,583,548,827],[316,686,560,615,350,525,132,727,417,538,275,760,678,369,700,841,869,124,371,770,844,794,470,530,315,46,187,397,789,802,906,258,596,280],[644,345,810,529,671,74,536,942,309,696,656,932,73,765,91,137,230,306,708,19,217,832,416,877,383,88,555,439,475,634,276,110,63,264],[308,358,748,808,610,48,772,317,11,10,752,355,100,355,237,345,66,525,564,459,309,329,450,807,751,295,512,339,879,577,917,348,226,942],[290,541,432,677,851,211,335,590,833,999,205,137,752,921,384,308,552,896,449,280,921,965,689,892,621,130,750,696,852,629,835,131,609,848],[234,293,375,545,959,683,172,381,689,541,33,18,80,17,911,200,933,555,575,343,444,881,410,784,245,581,71,875,797,599,554,20,220,172],[954,524,942,699,601,264,660,232,856,1000,962,734,688,698,539,863,956,686,62,966,819,223,425,380,925,206,107,109,828,647,813,130,49,238],[285,225,584,409,810,82,1000,216,996,895,897,849,38,325,292,779,915,738,176,868,461,660,521,114,901,858,592,684,77,311,540,373,788,947],[548,438,183,620,326,183,734,936,867,140,29,110,796,670,460,772,145,516,246,580,118,896,69,643,422,879,71,332,76,565,100,243,768,595],[394,378,11,372,474,863,352,164,96,5,444,655,815,949,637,768,906,678,225,320,637,253,283,998,866,12,856,377,720,495,476,669,590,727],[47,998,724,244,650,262,574,831,781,828,357,253,944,516,757,513,90,301,472,57,394,260,191,6,714,717,954,529,418,464,419,557,172,624],[233,428,411,604,348,847,439,448,582,688,16,477,79,39,973,436,177,614,934,648,219,908,97,67,604,827,404,340,259,718,595,31,630,500],[544,987,994,926,484,15,918,215,521,677,589,916,222,332,433,559,418,718,721,715,39,682,612,40,712,111,959,631,63,180,93,649,152,216],[49,140,179,140,701,568,924,508,49,560,358,211,828,998,262,511,846,450,696,128,488,296,393,103,233,499,361,109,318,104,853,928,748,752],[909,970,66,285,164,822,160,980,899,130,401,748,739,1000,31,191,464,623,571,950,954,684,727,579,678,660,516,253,914,424,277,824,611,628],[650,495,930,731,246,611,37,402,313,941,107,693,325,728,233,651,766,398,817,16,166,440,354,909,403,831,549,583,974,875,961,582,281,575],[674,276,587,499,266,399,650,846,675,573,882,576,103,279,262,209,980,594,60,830,37,940,306,50,505,551,975,425,928,859,809,445,283,640],[881,301,816,522,657,616,885,952,960,197,921,742,30,4,965,51,579,483,283,543,37,152,352,683,112,390,737,884,181,435,135,934,756,939],[19,372,395,683,922,616,907,295,560,575,331,54,336,375,221,135,411,430,434,410,44,598,714,736,846,699,777,577,876,611,689,892,660,469],[950,182,957,459,103,988,245,825,252,645,707,853,995,375,826,948,826,26,690,724,700,220,788,948,736,936,355,231,482,856,855,377,789,135],[50,649,686,288,269,579,887,320,360,939,808,508,264,2,336,571,554,52,304,162,859,548,405,325,605,163,799,500,558,307,120,61,220,826],[910,773,238,980,509,644,488,354,838,388,551,164,947,262,65,184,617,386,16,667,335,729,145,130,834,872,926,4,612,822,983,161,325,487],[701,512,194,180,843,552,625,544,455,226,904,502,912,341,581,360,61,830,115,65,173,970,198,97,268,665,556,768,235,534,657,32,716,796],[349,745,511,213,385,852,97,334,602,281,122,535,656,296,636,95,979,249,804,913,747,55,651,974,53,200,981,152,574,432,420,427,221,814],[23,989,485,40,31,359,682,246,182,667,114,520,562,578,156,321,999,661,56,879,700,753,290,527,515,932,714,369,269,758,795,959,98,401],[677,538,424,952,598,615,8,649,928,503,632,432,822,68,383,243,719,358,60,11,447,314,553,616,755,665,826,226,265,331,691,689,227,45],[787,115,809,967,960,954,426,412,465,394,944,78,577,283,120,63,224,818,420,399,218,629,817,715,402,551,415,286,388,831,879,720,86,704],[619,324,850,763,212,393,412,259,822,317,419,130,310,798,355,504,98,762,141,523,442,668,862,51,313,482,202,643,999,266,152,316,314,663],[364,690,222,857,332,466,565,226,595,958,818,889,668,303,322,100,516,753,792,295,83,25,421,386,478,895,369,998,278,63,899,87,142,129],[538,768,51,224,867,64,691,200,34,766,564,11,637,991,792,706,928,280,31,209,49,190,260,672,905,219,571,632,673,697,878,15,511,737],[47,313,507,174,323,362,966,850,797,852,400,26,196,358,96,987,728,666,194,854,85,839,224,54,414,373,665,184,110,264,872,297,390,969],[633,535,100,354,140,433,863,19,874,681,428,103,791,557,170,954,858,636,858,768,696,682,891,760,46,336,340,894,744,580,604,391,241,771],[458,587,372,424,456,237,395,416,138,625,82,261,124,718,960,504,675,427,90,665,563,235,273,103,412,443,807,274,196,898,883,722,849,115],[923,59,868,863,333,838,376,464,689,974,927,605,511,571,700,198,277,72,224,914,711,606,844,352,701,310,728,444,986,239,520,169,80,75],[171,293,216,884,637,275,741,231,722,630,621,28,383,685,629,178,663,89,742,476,757,108,663,591,260,71,363,687,440,512,177,716,794,511],[870,545,753,641,666,255,859,573,957,135,330,371,818,242,92,649,947,844,268,106,283,620,471,45,90,961,925,65,631,441,816,15,293,777],[658,489,12,672,798,706,378,711,700,653,512,150,638,719,327,806,438,472,938,299,635,836,364,314,795,2,148,81,596,619,443,594,463,542],[274,329,265,432,740,465,943,216,885,176,296,165,798,382,265,298,694,647,484,233,429,587,332,416,54,108,267,761,879,847,612,686,709,20],[247,354,478,648,363,740,510,29,320,808,264,471,987,12,550,820,247,962,932,841,513,222,905,354,622,139,841,667,984,981,365,986,606,910],[737,563,158,680,42,202,485,829,434,720,108,109,448,819,354,377,538,756,853,971,628,921,66,697,860,567,607,24,63,31,444,52,821,566],[767,474,755,981,833,780,696,953,854,58,285,913,215,824,813,97,276,462,818,477,808,925,309,764,375,532,356,447,443,287,457,214,42,980],[798,7,262,692,673,574,586,119,963,771,817,687,317,347,789,448,306,48,560,935,162,515,354,425,532,932,149,196,136,429,453,92,486,547],[788,274,446,909,767,892,91,161,600,528,143,786,545,198,33,733,121,822,769,132,708,486,684,363,79,122,234,43,319,2,953,114,173,873],[338,523,347,970,219,793,576,603,369,586,560,549,671,910,307,111,364,770,119,995,408,511,391,810,910,514,375,437,849,32,678,654,773,242],[665,171,891,446,764,506,430,463,890,859,196,933,807,952,66,455,74,707,941,419,234,130,333,715,22,504,551,346,335,914,914,853,975,126],[554,915,421,317,774,750,388,167,897,643,698,599,135,655,970,703,638,449,689,970,290,549,683,241,207,696,979,629,608,61,646,503,228,238],[994,874,695,751,566,707,419,948,293,716,762,235,54,37,712,612,437,218,508,659,515,210,297,843,842,835,381,375,32,314,935,847,954,268],[519,788,20,996,64,497,532,976,284,508,676,163,367,826,555,574,852,578,290,504,997,215,497,403,920,321,973,188,105,373,609,861,50,449],[485,921,323,717,364,249,962,411,693,654,454,383,715,303,610,112,434,141,925,571,643,768,947,276,518,455,3,1,431,779,169,870,334,3],[186,416,263,596,605,192,191,423,660,693,993,981,836,256,530,270,581,168,411,70,528,768,787,268,441,256,763,669,33,741,510,15,433,777],[298,554,115,312,723,98,817,514,239,629,108,430,733,378,25,227,548,302,547,741,217,832,196,798,903,722,191,229,810,257,654,914,974,110],[536,876,667,402,68,313,794,588,680,526,528,171,625,889,432,264,80,626,916,528,377,137,919,501,967,932,997,590,297,854,921,27,488,603],[999,847,936,481,325,199,907,897,678,688,672,466,103,308,206,94,744,545,514,54,680,653,584,877,959,324,460,200,849,787,957,385,168,531],[368,551,568,371,746,304,934,149,805,533,787,928,304,263,187,854,435,619,871,794,995,961,527,70,166,221,90,5,804,766,860,762,530,648],[302,523,659,1,104,584,269,61,667,529,957,758,592,308,263,714,801,16,284,535,432,192,478,715,343,189,339,298,375,880,127,431,609,47],[717,409,393,177,416,586,639,170,432,665,620,11,182,850,435,503,345,921,627,537,848,548,605,679,896,761,680,828,372,274,926,422,710,553],[404,431,977,531,402,811,158,422,410,394,818,55,429,982,805,619,598,439,593,670,275,809,20,806,124,611,39,120,422,245,827,99,380,999],[897,140,462,948,845,788,476,880,558,893,324,113,319,700,795,306,786,386,256,447,288,21,995,653,35,471,929,874,886,11,631,580,658,942],[290,423,317,542,512,929,718,599,175,482,471,500,101,908,641,919,12,403,646,983,819,427,170,732,705,436,805,40,342,280,155,80,882,954],[750,463,232,913,623,433,560,62,30,175,742,876,239,542,24,281,295,232,651,268,294,294,2,570,274,505,190,802,349,718,969,478,665,738],[724,119,989,716,760,15,338,622,638,513,816,357,105,111,431,129,44,230,57,741,664,703,319,156,891,63,164,165,417,649,247,199,280,494],[926,714,779,585,787,315,161,319,636,249,475,340,152,655,267,197,548,104,343,638,376,386,524,606,387,16,842,561,473,343,699,989,22,260]]
heights = [[366740,472793,823436,336361,66641,754272,848481,66438,872089,399882,961514,346768,276098,869376,418277,219992,861855,701031,13842,133214,302629,977405,617860,843277,920541,118845,251827,810705,669850,273587,29332,107186,222190,694960,533633,352756,111660,502240,123254,668616,162944,585834,676825,251925,391974,679329,942337,882767,699269,754403,856078,232208,836110,433299,422639,404161,485877,285837,219620,368411,789190,637605,280544,281906,429590,672283,565226,510330,136483,428077,204808,728606,737931,942155,367454,515967,879681],[298613,432086,394356,326178,698257,211272,477726,915110,489065,655153,489510,429495,561347,138414,429464,299204,423221,732440,766465,681363,234237,654579,949658,828456,843396,467246,119122,253643,60749,408470,564797,424954,406076,884610,177035,191726,391908,418546,356019,41989,367785,863696,350373,54455,515625,135079,916618,858157,63075,56881,976182,659247,730824,705084,442751,774621,46064,788099,862362,795132,904740,928512,431060,764922,652788,521775,938404,229982,990029,78078,648786,181095,980074,803659,833618,268044,722830],[590292,948715,466249,79279,679501,149964,698291,948728,217057,648369,970726,102777,886758,984753,60247,924206,337362,497695,671154,393941,681268,172227,108898,557375,550747,545243,300193,656070,828,821219,447638,971801,110701,603647,664053,998014,342110,611449,233459,979889,9962,188467,742919,324652,941195,801022,711136,291272,89839,990721,678263,778940,277069,882656,584516,791781,416040,435130,398962,557500,46038,854453,507607,671819,917337,466548,377268,724569,341545,553989,264864,576153,75316,570816,924790,304933,197937],[131897,833502,921742,155669,10814,824090,67790,576836,190790,898693,46131,127180,184369,956304,822901,844568,24467,217861,654466,251292,697018,206504,481080,49689,731591,172370,392200,45863,943020,749194,601115,508487,234659,10790,526796,71343,355300,406602,473546,56956,69410,443541,972444,401333,246510,151462,870684,423767,92382,554508,907833,272894,270116,428568,614623,488883,112934,26310,577999,596596,149071,626050,494969,747759,989293,947889,222760,541649,256356,482790,48197,925366,351943,147441,424555,929585,554797],[932300,345821,936278,472911,885012,632913,426169,766488,34328,244489,695670,950259,906863,470633,441387,361707,447498,985542,258152,921199,176990,487095,580863,78253,443492,128728,644519,196711,856611,13727,488107,129278,316579,903342,583472,544837,947000,97894,861497,253110,18095,282616,291255,383076,807746,307802,193501,195442,371205,564261,190017,791366,16522,796039,759085,403838,353225,914754,889841,92768,964220,410687,823981,340357,729342,388611,903231,702324,397867,135300,299104,683011,385676,982512,255694,90873,544273],[562660,94188,794152,406041,264086,889194,629697,445399,98182,64533,415821,62359,31077,147525,70801,872094,167548,468645,234241,961655,594536,152027,165222,80464,635445,511178,493639,397350,566855,933561,491168,564944,815199,910309,930831,176328,165447,772783,973773,361526,619921,39733,706252,43218,776625,146840,917403,285710,992498,207040,553432,869169,6840,565506,54146,881520,100775,775763,431592,605314,557294,158061,521022,344908,571028,286774,695794,359496,499194,934381,71165,432196,7987,627854,356117,108191,614202],[972154,226926,413428,887756,318785,263077,533199,50198,285351,278273,156201,233049,603794,181325,487175,702068,268395,704499,594308,822013,688046,896009,410959,389363,491810,440374,708562,5862,121257,308183,330886,925463,821569,380558,199606,128819,251051,976685,197358,979613,7242,247347,646586,970362,717090,340342,883512,961705,230536,10856,752897,262988,365599,248892,711694,742773,99357,93015,613995,74581,115114,839840,283615,792884,12014,967740,285797,621488,311623,969994,294069,915555,37352,465108,160901,272419,567424],[617844,364929,870751,236492,831947,539873,196765,440312,513170,749545,124455,271866,325056,411886,832171,682235,462861,373867,224860,781518,206661,222580,142656,743822,661628,600615,934803,483942,616738,354486,649556,378386,1412,300974,201998,467798,797010,507531,55926,769828,365872,402833,721366,982501,152846,852134,213993,61812,183894,11982,523617,533502,527789,865738,15988,866679,888489,362850,455221,868985,312422,42544,696254,132789,354694,173641,855921,449110,909735,167573,893246,952653,123855,932476,299262,157054,450207],[152325,654141,123157,142296,480328,487423,122721,424880,831939,543177,1885,347313,67083,863048,513654,238629,607352,389609,38944,860119,155126,448782,164480,619532,264858,123108,611898,825991,722539,163269,939349,412669,896926,757637,138604,510683,573377,622116,637190,463276,914777,414394,707899,337611,655455,703047,717441,743624,458680,241053,12864,695717,12936,153583,457278,67347,641828,337669,817193,987667,60994,687220,312389,242900,959456,952830,268532,488665,361269,601636,153588,243955,411169,385191,441850,341831,252385],[398147,376849,765369,470052,688610,200296,430730,888055,206411,32844,94503,620269,172991,821101,7761,531113,819970,115397,807407,26237,679821,184994,243463,726015,715956,492877,510174,628494,986993,857848,946850,74280,322364,569777,559388,176105,247043,150877,364819,915623,637768,866251,893584,453246,227315,544553,995289,309182,804205,528803,577792,936961,219447,212878,85470,449239,539079,16047,894941,605422,857185,86941,649536,726695,832604,961255,235264,634640,875111,62598,883415,163499,626029,118393,387561,380498,984844],[285043,635334,73864,643553,651289,659929,357023,43068,229234,76904,302496,34120,377967,968008,144840,70437,246832,695236,308804,214051,779875,937525,97192,882525,904838,577530,253168,79183,804803,428416,232814,840415,353054,833627,849517,24439,297940,939514,9765,135179,748143,802161,757404,407907,257842,125107,120118,151146,400108,468020,336232,968157,11015,745866,676568,203765,9368,431981,177552,678808,822185,286703,979001,487645,940711,886504,3387,27854,303945,536378,11448,189773,461741,655651,106832,840909,604699],[84890,982776,371518,914377,102272,639561,347809,172460,698814,303076,235085,841109,930161,40617,910244,476590,624619,523468,565977,305651,85362,391467,783775,580512,551582,425436,295733,396859,731395,875499,607722,141677,252840,119533,26882,449387,859038,888763,119775,124272,176426,759688,304788,857093,466458,547576,924786,19019,521699,262419,758186,976674,754842,828755,476171,361254,395409,948669,648034,852589,65888,114937,508517,753619,607857,342800,828167,737598,109561,96018,524798,92798,771984,364592,986092,207587,128077],[172184,664707,687689,210478,667335,809084,620970,943489,33981,492367,845922,844175,604025,522331,680575,482020,986325,512471,161061,360940,202144,626635,25951,170043,828689,587310,48663,171915,149532,473371,877325,483925,503848,619643,658054,413091,101163,865286,777113,322972,721696,297887,370566,359353,766519,866555,468515,761998,448229,773174,768866,167993,556399,847703,614335,688744,978217,717950,11748,931287,346279,370405,562363,57812,227695,211295,239948,65635,150940,749508,754105,316214,870943,919721,503924,479138,177465],[226251,777559,98765,813677,298519,475246,607587,987386,780374,109426,635462,302699,962325,758169,851846,401598,332062,718336,901685,811000,23935,449366,552161,817064,322891,43824,104470,896201,694064,926122,434893,383796,4004,485284,987804,795653,418812,530008,461715,486471,568226,90871,799199,886247,890237,275883,291692,100405,453031,483350,934165,54914,323450,528761,36341,703435,422764,706338,372109,620495,384279,992079,368704,349503,345439,101669,203780,274992,948792,558071,894341,433634,46390,119518,118635,363862,971380],[579471,139821,88762,217947,652684,447186,288831,827814,538899,866321,697943,495086,958952,823019,555530,83584,219247,558004,710211,205031,17002,765046,432556,631789,157700,348125,191823,489987,224424,30781,38862,536543,122120,826634,911268,600168,844758,607545,192155,145516,628678,197471,600424,470093,255690,651017,527206,72982,427390,225457,596501,626159,703238,622410,258701,371503,148062,627027,383354,186407,217904,643381,497431,296235,200290,509699,388847,180258,353591,113464,545007,181806,502202,914339,582939,792172,49219],[162012,196692,670800,174060,327036,877457,64949,86952,586809,148048,718605,953017,774736,988556,225778,17454,566490,531289,34834,416962,623487,898126,102994,384896,779249,737872,633236,433715,760885,933871,177291,457227,335680,499308,828840,801763,323848,405901,352526,714305,470314,239833,741690,548070,887354,386878,594182,940394,337501,717274,459365,620118,753637,170025,158882,725462,90552,312528,229559,668547,104024,200723,609109,616037,484396,460754,163337,765808,409771,936303,528606,253741,905475,450433,691527,332556,279005],[805638,469194,652587,199542,277657,863467,500672,299695,610146,48430,507819,221215,951410,415423,582479,21827,186156,762859,85269,574095,432001,988259,547302,73946,769846,496804,248596,584287,260377,705829,943790,129556,411235,795052,146407,487325,918541,659300,472936,783610,314665,765395,129982,219384,939605,100776,946367,65438,110885,794080,569986,577607,955082,288555,587246,388387,277273,612735,555865,976732,838477,676309,568366,496331,166556,383914,348025,177705,973413,436202,228042,54050,554484,425162,766921,745122,847316],[652015,254147,171919,164461,857784,775707,37340,80756,248379,137778,547338,225533,848283,195525,371276,557061,883818,2662,417684,657915,658163,403195,545325,635580,367756,145466,719675,630598,677159,360051,28770,237392,52607,497933,184697,832549,233300,889048,338449,727394,559192,750777,465835,989199,308131,633326,801245,411976,666610,21830,971440,647541,128431,761573,239128,564560,791258,982273,174248,576278,985924,260143,519473,696606,423105,215338,496290,74771,281836,246629,406162,618627,380793,728982,70531,496539,815483],[706726,941531,335166,95154,449779,260558,162628,886410,900814,195483,735920,108832,828567,36945,610776,628820,533897,48259,141984,316885,341148,364423,814220,473030,461721,156934,786874,604054,462794,987089,695332,657682,815050,762071,453218,233808,688793,661521,414307,183718,101539,123253,857784,108068,355872,86921,75630,599397,350409,762837,20651,734317,51594,744020,702220,738749,755409,115049,631544,906727,463405,763990,519496,995771,70638,59455,276958,40333,234770,768243,548987,116920,386197,174678,403440,880776,222407],[329055,869210,455850,283973,800136,673287,169809,197758,46610,44198,489137,684673,966233,817568,5294,439746,491926,837884,257164,299933,805218,171177,875336,260248,47139,679331,566428,114276,933804,332943,875639,64398,944182,436804,398701,386939,823947,447629,458078,709023,54068,781937,730115,141319,506910,748496,279668,505209,525274,942561,404136,707686,185448,281308,677324,147158,643973,671470,46462,55244,666262,238704,990887,546117,475341,162022,560248,737979,544341,279435,584268,82224,546293,100134,761153,532095,524360],[475232,620090,236100,20075,474111,643713,394016,70032,298183,359995,922827,344352,368478,67308,249405,570431,242378,730144,779361,317885,43735,20520,473688,738825,810851,83776,636893,10306,776521,775020,168973,167665,530985,208984,581241,530306,277808,737255,380394,345427,237937,579659,374094,843600,208929,578333,887202,878079,9256,624116,804540,429799,814833,429570,918741,102920,580150,566398,258477,949237,298475,497457,393797,993233,56323,618493,963927,324649,519296,199842,428051,112996,248649,98153,821956,966948,502625],[762982,901490,946053,680064,773005,656235,198454,26196,219120,12625,95284,454158,545559,175643,565393,576719,893937,879581,656178,710025,984215,466153,61351,505191,276650,483831,933113,353601,918898,289949,504337,369599,868773,353772,70611,343958,305746,26649,817091,233960,406406,877281,852389,372479,370056,355058,198286,617426,576585,308243,562049,220756,927204,988861,461935,145254,768999,89090,493949,956032,281459,513368,848525,292508,144367,718299,729531,243557,480806,951480,190816,488360,814501,931128,446290,816900,516211],[507851,534658,294981,108200,532671,433100,661483,623935,578468,266328,348169,25430,270722,295367,69600,298125,892886,780662,732744,274600,804537,847226,589837,890979,380941,355372,825066,20777,932534,306721,604408,193713,661294,761819,149847,747130,607682,340535,140080,805794,221626,838218,459662,84415,488570,993639,785439,578957,90167,760854,547388,873209,556386,121076,936608,146076,559458,22289,994735,630789,904992,651499,744570,953586,995200,225007,748179,786022,600034,533273,419207,607854,495976,428199,512090,224364,408396],[745179,90384,599331,416610,942222,931724,913961,575154,164972,651898,352202,465837,465196,27173,587965,851740,357954,353923,196404,174302,781494,697532,766234,350318,408711,652532,149815,702841,464110,699925,245638,406017,713484,911846,33413,978153,574988,530754,462109,539541,314059,812135,645773,267510,640487,225722,225310,383384,41277,427304,830872,697364,917765,523305,839151,490116,703868,191449,806100,758705,483395,758997,734696,977181,957348,772734,115649,31742,148832,632509,470982,293071,559104,908424,205496,910894,971223],[353362,371187,376631,456703,763744,615258,109028,696707,8603,464013,124792,37709,700052,622270,910608,100984,334583,514610,397787,855837,295154,784223,873648,757493,429979,716992,692617,201258,351725,677268,188240,889394,970854,899087,676107,575493,120993,839984,172317,969152,238509,618320,671174,649074,169153,87571,844656,853486,956435,773787,294601,384932,912612,637620,927922,329361,204482,224572,890525,228608,406891,388282,250152,341092,117961,773933,415853,818325,842009,903513,918358,200643,529835,654591,881983,299574,673498],[242102,925447,791642,592980,260040,29701,159007,516947,735770,253342,44446,148749,7760,162019,835343,105587,399907,451913,720371,64172,295600,287227,470636,255635,896259,95321,601401,20020,151358,107801,504759,508831,178187,679958,807519,668150,889670,58290,968167,813183,540457,254660,238956,744629,360126,476490,29534,215341,6780,228667,146448,332279,450604,938999,595241,875827,502534,979636,588585,391932,45608,909324,19140,561822,941858,823154,829731,959052,204640,868350,398808,910944,344049,585883,678668,397866,935926],[198054,380299,221654,935637,596820,528825,255564,472313,643285,737373,938283,965573,415430,828865,995205,63185,347651,769935,473437,877669,93515,323866,87684,860084,713548,752634,357899,368505,655903,415404,704369,972697,569659,409236,322040,279744,90514,664979,869094,235087,35340,247015,790223,80464,280547,197717,661272,112714,346219,30148,246377,10586,244332,986860,652004,28001,19194,111413,910342,560400,388928,748395,683712,954630,842357,496069,10897,111947,464574,244110,700978,72905,850417,800805,146117,589082,50592],[91169,310822,458365,842770,829849,94621,165745,753863,225036,368242,413089,552416,52267,701181,512909,490143,155703,881563,712962,815434,607446,264980,510883,66554,424416,196777,310124,448927,956737,366642,919372,675578,899879,814622,986567,815697,571436,215954,550629,90467,790289,789530,905859,418898,274725,902433,739242,656536,120325,519319,36185,54727,547607,711499,969158,940677,456995,48886,360532,855940,230735,595703,243629,808931,520322,266895,894186,54912,13890,854377,615996,738757,574910,13498,159100,936276,634433],[686660,934293,730162,630598,713054,636975,794854,651818,16060,71338,771725,74723,688596,821715,379725,928753,582261,662872,394141,125161,686768,779726,39898,300612,350980,665778,48634,695226,44469,125326,224170,206009,894229,816146,306017,726392,209856,690159,791378,779106,549626,524726,548405,687409,570902,384250,834153,749372,270659,481883,496933,690683,920595,130051,525,520379,693797,918492,952914,530328,383106,234571,950921,886026,394361,216039,826827,194674,962648,393975,182555,109740,893915,291324,852160,510727,449792],[652885,55577,93331,406490,624987,227193,343873,839213,876299,649316,762618,272458,924985,313128,324069,64344,590175,570662,609769,605621,79931,924970,186957,537425,94416,1477,424061,34513,119490,292632,122301,141442,720188,102183,705999,396582,939240,966239,66969,922634,587259,718056,519502,932982,412054,730514,576665,729783,736708,342910,342923,571887,342901,632045,13878,969449,276231,316039,876246,612874,738640,919265,280504,130038,351604,718272,7136,431372,269230,500021,295145,776904,875929,611823,465449,318433,113366],[481773,964200,248789,607758,73391,612092,494792,961654,476835,282242,605135,559720,355866,387067,661761,594121,130259,550291,184345,331644,485945,937815,841720,462955,193402,338146,705567,938593,412699,555450,465549,969815,830551,605412,44599,434639,235216,51290,775137,292933,988348,824003,633498,605809,685858,63617,801016,538173,167259,943035,554281,265762,847994,178341,234402,812649,515540,249424,763026,656591,544863,816414,33932,435230,841656,917385,413643,635492,705073,635904,881783,197598,89156,862053,9324,414699,374924],[319451,936630,184842,871739,704434,62234,297318,112618,814962,597367,798754,868452,345080,385729,979653,161649,515055,402336,658119,93687,456870,181342,78546,956338,201290,668637,690560,638404,359457,863763,980774,555070,668201,915354,495920,593706,555385,352821,898339,992648,528809,585459,76357,961707,217510,288075,702917,672317,524580,819511,413810,821206,701418,914021,740006,952313,695067,559747,993169,250877,152447,679961,775413,508681,848040,868588,942752,531150,728498,847052,625108,734159,499529,794623,552449,827444,500678],[308832,282564,474166,885096,353456,536965,917144,579894,315149,361190,853456,930903,606807,983388,974598,897829,128735,200626,997946,982405,724071,530633,391227,630089,402213,757866,668911,784368,197328,377291,752462,683437,813550,260480,502834,862592,794593,253874,55250,506775,355034,675190,582299,659251,568950,363825,447099,880025,745004,292294,41383,801931,470755,944512,681705,251572,435581,815733,812026,153534,614895,555354,541180,989842,146195,782339,386498,981179,31661,341366,609924,716130,305133,435207,337400,23584,848424],[512436,753405,255788,650130,110554,572675,330743,984259,743275,849575,415211,145590,479920,3519,728393,722545,746735,102174,409734,479541,875816,910324,195751,766045,346803,117001,226401,556713,916076,80754,407023,684028,390759,637575,642968,258400,576391,192760,357173,696624,418251,66651,517181,300935,704879,388971,576545,905714,319460,666789,116572,104753,525626,293141,908979,781486,687765,624208,252615,299427,184042,881431,462503,820481,358394,972529,947314,638655,838909,634499,294869,78100,417157,340933,62442,351865,115587],[521516,577895,79643,853419,522504,96712,173414,50838,340749,106717,90788,381311,447921,911743,771316,328311,838499,585413,310854,451424,992719,808295,807218,381509,477495,609304,929978,529827,648649,213230,548961,783360,198717,155765,780314,680168,853764,700433,24073,126756,783895,244982,911897,530846,593919,344448,881861,841474,459127,67313,232212,16272,765794,597972,178997,62398,340196,67426,649651,127814,573602,131701,707356,454835,718421,324956,338719,363870,60112,236548,178939,469412,605650,923259,922470,75621,916908],[707246,662541,507010,853496,550957,958756,903915,952569,468178,247037,425189,859096,479594,307971,237718,519153,678451,75102,820818,887755,288438,387180,94251,353475,190963,319830,233085,883830,722309,830327,737877,902440,482577,173135,420640,623432,874932,270507,572371,489758,866397,982628,517304,906598,405572,407118,736451,129767,245934,104753,72142,365307,264893,420034,938689,225212,972425,660068,991504,404256,742240,334890,239915,39967,205573,924882,82091,723496,161980,909997,211900,73977,217503,518674,229163,439472,775938],[695670,628008,252939,994358,645947,419900,903631,549230,529798,636931,830311,397001,503829,875965,320383,729956,231772,979028,853322,896811,346857,499151,10501,273531,532770,292814,654021,954280,221109,701569,167039,943684,522194,644634,425045,150123,606808,701382,202063,246186,127221,502898,213484,869389,649474,464785,593913,237484,468507,471809,915004,767266,610025,595914,388921,47526,638261,475879,271867,65892,973872,244086,569260,79004,636111,86117,678432,224626,462938,540293,745673,475946,23208,889748,498594,78340,98466],[871893,805030,480823,464614,35121,317268,996581,409428,806377,680516,514732,601874,370133,140166,135064,940817,96027,122160,246830,998323,123394,663032,741953,347926,848561,761541,707447,157734,433037,921035,996509,952022,233631,173518,817945,595788,587129,783424,359138,882504,892247,260219,10334,139827,416427,552032,140196,703262,416688,586377,114001,357195,135405,801856,160290,790195,634111,274745,344607,809643,87014,890689,351197,436065,448009,715432,157187,269773,859061,82222,111295,851557,535719,486234,315971,718530,801253]]






so = Solution()
r = so.minimumEffortPath(heights)
pp.pprint(r)


time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)
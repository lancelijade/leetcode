from collections import Counter


class Solution:
    def minSwaps(self, data: list[int]) -> int:
        t = Counter(data)
        if t[1] == 1: return 0
        #print(t)
        i = 0
        j = t[1]
        t1 = Counter(data[i:j])
        #print(t1)
        if 0 not in t1: return 0
        mi = t1[0]

        while j < len(data):
            
            if data[i] != data[j]:
                if data[i] == 1:
                    t1[1] -= 1
                else:
                    t1[0] -= 1

                if data[j] == 1:
                    t1[1] += 1
                else:
                    t1[0] += 1

            if 0 in t1 and t1[0] != 0: 
                mi = min(mi, t1[0])
            else:
                return 0

            #print(i, j, t1, data[i], data[j])


            i += 1
            j += 1
        
        return mi


data = [1,0,1,0,1,0,0,1,1,0,1]
data = [0,0,0,1,0]
data = [1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]


so = Solution()
r = so.minSwaps(data)
print(r)
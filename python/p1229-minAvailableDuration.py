class Solution:
    def minAvailableDuration(self, slots1: list[list[int]], slots2: list[list[int]], duration: int) -> list[int]:
        i = 0
        j = 0
        slots1.sort()
        slots2.sort()

        while i < len(slots1) and j < len(slots2):

            a1, b1 = slots1[i]
            a2, b2 = slots2[j]

            print(i, a1, b1, j, a2, b2)

            if a1 > b2:
                j += 1
                continue
            elif a2 > b1:
                i += 1
                continue

            amax = max(a1, a2)
            bmin = min(b1, b2)
            if bmin - amax >= duration:
                return [amax, amax+duration]
            elif a1 == a2:
                if b1 > b2:
                    i += 1
                    continue
                else:
                    j += 1
                    continue
            elif b1 > b2:
                j += 1
                continue
            else:
                i += 1
                continue
                
        return []



slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 8

"""
slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 12

slots1 = [[0,2]]
slots2 = [[1,3]]
duration = 1

slots1 = [[10,60]]
slots2 = [[12,17],[21,50]]
duration = 8
"""

slots1 = [[216397070,363167701],[98730764,158208909],[441003187,466254040],[558239978,678368334],[683942980,717766451]]
slots2 = [[50490609,222653186],[512711631,670791418],[730229023,802410205],[812553104,891266775],[230032010,399152578]]
duration = 456085



so = Solution()
r = so.minAvailableDuration(slots1, slots2, duration)
print(r)
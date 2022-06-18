
from collections import deque

class Solution:
    def wordsAbbreviation(self, words: list[str]) -> list[str]:
        
        def abbr(word, prefix_len):
            w = word[:prefix_len] + str(len(word) - prefix_len - 1) + word[-1]
            return word if len(w) >= len(word) else w

        d = {}
        todo = deque()
        prelen = 1
        for i, word in enumerate(words):
            w = abbr(word, prelen)
            if w in d:
                d[w].append((word, prelen, i))
            else:
                d[w] = [(word, prelen, i)]

            if len(d[w]) > 1 and w not in todo:
                todo.append(w)

        while todo:
            #print(todo)
            k = todo.popleft()
            for word, prelen, i in d[k]:
                w = abbr(word, prelen+1)
                if w in d:
                    d[w].append((word, prelen+1, i))
                else:
                    d[w] = [(word, prelen+1, i)]

                if len(d[w]) > 1 and w not in todo:
                    todo.append(w)

            del d[k]

        #print(d)

        dd = sorted(d.items(), key=lambda x: x[1][0][2])
        return [x for x, _ in dd]


words = ["like","god","internal","me","internet","interval","intension","face","intrusion"]
#words = ["aa","aaa"]
words = ["abcdefg","abccefg","abcckkg"]

so = Solution()
r = so.wordsAbbreviation(words)
print(r)
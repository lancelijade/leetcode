#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#

import pprint
from typing import OrderedDict
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
class Codec:

    def __init__(self):
        self.prefix = "http://go.com/"
        self.prelen = len(self.prefix)
        self.map = OrderedDict()

    def encode(self, longUrl: str) -> str:
        h = str(hash(longUrl))
        self.map[h] = longUrl
        return self.prefix + h
        

    def decode(self, shortUrl: str) -> str:
        if shortUrl[:self.prelen] != self.prefix: return False
        return self.map[shortUrl[self.prelen:]]
        

# @lc code=end

url = "https://leetcode.com/problems/design-tinyurl"

codec = Codec()
ue = codec.encode(url)
print(ue)
print(codec.decode(ue))


time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)
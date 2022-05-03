import pprint
from executing import Source
pp = pprint.PrettyPrinter()
from var_dump import var_dump
from collections import OrderedDict
import math
import heapq
from collections import deque
from datetime import datetime 
time_start = datetime.now()


class FileSystem:
    
    def __init__(self):
        self.fs = {}

    def createPath(self, path: str, value: int) -> bool:
        if len(path)<2 or path[0]!="/" or path in self.fs:
            return False

        parts = path.rsplit('/', maxsplit=1)
        if parts[0] and parts[0] not in self.fs:
            return False

        self.fs[path] = value
        return True

    def get(self, path: str) -> int:
        if path not in self.fs:
            return -1
        else:
            return self.fs[path]



fileSystem = FileSystem();

print(fileSystem.createPath("/leet", 1)); # return true
print(fileSystem.createPath("/leet/code", 2)); # return true
print(fileSystem.get("/leet/code")); # return 2
print(fileSystem.createPath("/c/d", 1)); # return false because the parent path "/c" doesn't exist.
print(fileSystem.get("/c")); # return -1 because this path doesn't exist.


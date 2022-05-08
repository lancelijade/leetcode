#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#




class NestedInteger:
    def isInteger(self) -> bool:
        1
    def getInteger(self) -> int:
        1
    def getList(self) -> list[int]:
        1

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# @lc code=start

class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):

        def flat(li: list[NestedInteger]):
            for l in li:
                if l.isInteger():
                    self.li.append(l.getInteger())
                else:
                    flat(l.getList())

        self.li = []
        self.p = -1
        flat(nestedList)

   
    def next(self) -> int:
        self.p += 1
        return self.li[self.p]
        
    
    def hasNext(self) -> bool:
        return self.p + 1 < len(self.li)
         


# @lc code=end

# Your NestedIterator object will be instantiated and called as such:

#i, v = NestedIterator(nestedList), []
#while i.hasNext(): v.append(i.next())
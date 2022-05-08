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

class NestedIterator2:
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
         

class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        self.p_st = []
        self.p = -1
        self.li_st = []
        self.li = nestedList


    def next(self) -> int:
        if self.p + 1 < len(self.li):
            self.p += 1

            if self.li[self.p].isInteger():
                #print(self.li[self.p].getInteger())
                return self.li[self.p].getInteger()
            else:
                self.li_st.append(self.li)
                self.li = self.li[self.p].getList()
                self.p_st.append(self.p)
                self.p = -1
                return self.next()     

        elif self.li_st:
            self.li = self.li_st.pop()
            self.p = self.p_st.pop()
            return self.next()

    
    def hasNext(self) -> bool:
        if self.p + 1 < len(self.li):
            if self.li[self.p+1].isInteger():
                return True
            else:
                self.li_st.append(self.li)
                self.li = self.li[self.p+1].getList()
                self.p_st.append(self.p+1)
                self.p = -1
                return self.hasNext()                 
        elif self.li_st:
            self.li = self.li_st.pop()
            self.p = self.p_st.pop()
            return self.hasNext()
        else:
            return False


# @lc code=end

# Your NestedIterator object will be instantiated and called as such:

#i, v = NestedIterator(nestedList), []
#while i.hasNext(): v.append(i.next())
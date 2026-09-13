# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is provided, initializes a single integer holding value.
#        Otherwise, initializes an empty nested list.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if not s:
            return NestedInteger()
        
        # Handle standalone integer case
        if s[0] != '[':
            return NestedInteger(int(s))
        
        stack = []
        num_str = ""
        
        for char in s:
            if char == '[':
                stack.append(NestedInteger())
            elif char in (',', ']'):
                if num_str:
                    stack[-1].add(NestedInteger(int(num_str)))
                    num_str = ""
                
                if char == ']' and len(stack) > 1:
                    completed_list = stack.pop()
                    stack[-1].add(completed_list)
            else:
                num_str += char
                
        return stack[0]
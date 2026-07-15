class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        # Base index for calculation
        stack = [-1]
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # Current ')' is a boundary, push its index as the new base
                    stack.append(i)
                else:
                    # Current valid length is current index minus the last base index
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len
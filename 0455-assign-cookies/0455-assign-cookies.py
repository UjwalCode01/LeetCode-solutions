class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        
        child_ptr = 0
        cookie_ptr = 0
        
        while child_ptr < len(g) and cookie_ptr < len(s):
            # If the cookie satisfies the child's greed
            if s[cookie_ptr] >= g[child_ptr]:
                child_ptr += 1  # Move to the next child
            
            cookie_ptr += 1  # Move to the next cookie regardless
            
        return child_ptr
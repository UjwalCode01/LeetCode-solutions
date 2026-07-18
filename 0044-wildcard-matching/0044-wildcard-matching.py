class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :type rtype: bool
        """
        s_ptr, p_ptr = 0, 0
        match_idx = 0
        star_idx = -1
        
        while s_ptr < len(s):
            # Case 1: Characters match, or pattern has '?' (matches any single character)
            if p_ptr < len(p) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            
            # Case 2: Pattern has '*', track its position and try matching 0 characters first
            elif p_ptr < len(p) and p[p_ptr] == '*':
                star_idx = p_ptr
                match_idx = s_ptr
                p_ptr += 1  # Advance pattern pointer past the '*'
            
            # Case 3: Current characters don't match, but we saw a '*' earlier.
            # Backtrack: force the previous '*' to match one more character in string `s`.
            elif star_idx != -1:
                p_ptr = star_idx + 1  # Reset pattern pointer to right after the '*'
                match_idx += 1        # Increment the matched segment length
                s_ptr = match_idx     # Reset string pointer to the new match position
                
            # Case 4: Characters don't match, and there's no '*' to fall back on
            else:
                return False
                
        # Consume any remaining trailing '*' characters in the pattern
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
            
        # If we successfully traversed the entire pattern, it's a match
        return p_ptr == len(p)
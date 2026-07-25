class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        
        # Early exit: IP address length must be between 4 and 12
        if len(s) < 4 or len(s) > 12:
            return res
            
        def backtrack(start, current_parts):
            # If we have 4 parts and used all characters, save the valid IP
            if len(current_parts) == 4:
                if start == len(s):
                    res.append(".".join(current_parts))
                return
            
            # Try segment lengths of 1, 2, and 3
            for length in range(1, 4):
                if start + length > len(s):
                    break
                    
                segment = s[start:start + length]
                
                # Check for leading zero: length > 1 and starts with '0'
                if len(segment) > 1 and segment[0] == '0':
                    continue
                    
                # Check numerical range
                if int(segment) <= 255:
                    current_parts.append(segment)
                    backtrack(start + length, current_parts)
                    current_parts.pop()
                    
        backtrack(0, [])
        return res
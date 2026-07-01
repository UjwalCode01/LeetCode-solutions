class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        first_str = strs[0]
        
        for i in range(len(first_str)):
            char = first_str[i]
            
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return first_str[:i]
                    
        return first_str
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        
        def backtrack(start, path):
            if start == len(s):
                res.append(list(path))
                return
            
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                # Check if the substring is a palindrome
                if sub == sub[::-1]:
                    path.append(sub)
                    backtrack(end, path)
                    path.pop()  # Backtrack
                    
        backtrack(0, [])
        return res
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Store the last occurrence index of each character
        last_index = {char: i for i, char in enumerate(s)}
        
        stack = []
        visited = set()
        
        for i, char in enumerate(s):
            # Skip if character is already part of the result
            if char in visited:
                continue
                
            # Pop larger characters if they appear again later in s
            while stack and stack[-1] > char and last_index[stack[-1]] > i:
                removed_char = stack.pop()
                visited.remove(removed_char)
                
            stack.append(char)
            visited.add(char)
            
        return "".join(stack)
from collections import deque

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        result = []
        visited = set([s])
        queue = deque([s])
        found = False

        while queue:
            curr = queue.popleft()

            if isValid(curr):
                result.append(curr)
                found = True

            # If we already found valid strings at this level, don't generate shorter ones
            if found:
                continue

            # Generate all possible states by removing one parenthesis
            for i in range(len(curr)):
                if curr[i] not in ('(', ')'):
                    continue
                
                next_str = curr[:i] + curr[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)

        return result
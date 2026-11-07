class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        answer = [float('inf')] * n
        
        # Pass 1: Scan from left to right to find distance to the closest 'c' on the left
        prev = -float('inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], abs(i - prev))
            
        # Pass 2: Scan from right to left to find distance to the closest 'c' on the right
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], abs(i - prev))
            
        return answer
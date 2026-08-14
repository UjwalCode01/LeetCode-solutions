class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        memo = {}  # Stores (r, c) -> longest path starting at (r, c)
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(r, c):
            # Return cached result if already computed
            if (r, c) in memo:
                return memo[(r, c)]
            
            max_len = 1  # Base case: every cell has a path of length at least 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check boundaries and strictly increasing condition
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))
            
            memo[(r, c)] = max_len
            return max_len
        
        longest = 0
        for r in range(rows):
            for c in range(cols):
                longest = max(longest, dfs(r, c))
                
        return longest
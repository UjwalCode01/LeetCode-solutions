class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Step 1: Ensure every row starts with a '1' (toggle row if it starts with '0')
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]
                    
        # Step 2: For each column from index 1 onwards, ensure the count of '1's 
        # is greater than or equal to the count of '0's (toggle column if needed)
        for j in range(1, n):
            ones_count = sum(grid[i][j] for i in range(m))
            if ones_count < m - ones_count:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]
                    
        # Step 3: Calculate the final score by summing the binary value of each row
        score = 0
        for i in range(m):
            row_value = 0
            for j in range(n):
                row_value = (row_value << 1) | grid[i][j]
            score += row_value
            
        return score
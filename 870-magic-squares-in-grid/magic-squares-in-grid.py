class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def is_magic(r, c):
            # Fast check: center must be 5
            if grid[r + 1][c + 1] != 5:
                return False
            
            # Collect numbers and check range [1, 9]
            nums = []
            for i in range(3):
                for j in range(3):
                    nums.append(grid[r + i][c + j])
            
            if sorted(nums) != list(range(1, 10)):
                return False
            
            # Check rows and columns sum
            for i in range(3):
                if sum(grid[r + i][c + j] for j in range(3)) != 15:
                    return False
                if sum(grid[r + j][c + i] for j in range(3)) != 15:
                    return False
            
            # Check diagonals sum
            if (grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2]) != 15:
                return False
            if (grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c]) != 15:
                return False
                
            return True

        count = 0
        # Loop through all possible top-left corners of 3x3 subgrids
        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic(r, c):
                    count += 1
                    
        Id = count
        return count
class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        # Get the number of rows and columns
        rows, cols = len(matrix), len(matrix[0])
        
        # Check every element against its top-left neighbor
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] != matrix[r - 1][c - 1]:
                    return False
                    
        return True
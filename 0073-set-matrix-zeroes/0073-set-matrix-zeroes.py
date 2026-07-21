class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        # 1. Check if the first column needs to be zeroed
        for r in range(ROWS):
            if matrix[r][0] == 0:
                first_col_zero = True
                break

        # 2. Check if the first row needs to be zeroed
        for c in range(COLS):
            if matrix[0][c] == 0:
                first_row_zero = True
                break

        # 3. Use first row & first column as markers for the inner matrix
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # 4. Zero out cells based on markers in the first row & column
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # 5. Handle the first column if it contained zero originally
        if first_col_zero:
            for r in range(ROWS):
                matrix[r][0] = 0

        # 6. Handle the first row if it contained zero originally
        if first_row_zero:
            for c in range(COLS):
                matrix[0][c] = 0
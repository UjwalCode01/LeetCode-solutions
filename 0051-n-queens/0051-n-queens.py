class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # Tracking sets for fast O(1) lookups
        cols = set()
        pos_diags = set()  # Tracks (row + col) diagonals (bottom-left to top-right)
        neg_diags = set()  # Tracks (row - col) diagonals (top-left to bottom-right)
        
        result = []
        # Initialize an empty board represented as an array of dots
        board = [["."] * n for _ in range(n)]
        
        def backtrack(row):
            # Base Case: If we successfully placed queens in all rows, save the state
            if row == n:
                copy = ["".join(r) for r in board]
                result.append(copy)
                return
            
            for col in range(n):
                # Check if the current cell is under attack
                if col in cols or (row + col) in pos_diags or (row - col) in neg_diags:
                    continue
                
                # 1. Place the queen
                cols.add(col)
                pos_diags.add(row + col)
                neg_diags.add(row - col)
                board[row][col] = "Q"
                
                # 2. Recurse to place a queen in the next row
                backtrack(row + 1)
                
                # 3. Backtrack (remove the queen and clean up sets)
                cols.remove(col)
                pos_diags.remove(row + col)
                neg_diags.remove(row - col)
                board[row][col] = "."
                
        # Start backtracking from the 0th row
        backtrack(0)
        return result
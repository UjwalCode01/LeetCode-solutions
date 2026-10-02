class Solution(object):
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        # Directions for the 8 neighbors
        neighbors = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        # Pass 1: Mark state changes with intermediate values
        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0
                
                # Count live neighbors in original state
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] in (1, 2):  # Was originally live
                            live_neighbors += 1
                
                # Rule application
                if board[r][c] == 1:
                    # Under-population (< 2) or Over-population (> 3)
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2  # Dies
                else:
                    # Reproduction (= 3)
                    if live_neighbors == 3:
                        board[r][c] = 3  # Becomes alive
                        
        # Pass 2: Finalize state updates
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1
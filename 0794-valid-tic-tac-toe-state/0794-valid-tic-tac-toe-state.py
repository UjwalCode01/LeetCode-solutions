class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        x_count = sum(row.count('X') for row in board)
        o_count = sum(row.count('O') for row in board)
        
        # X goes first and takes turns alternating with O
        if not (o_count <= x_count <= o_count + 1):
            return False
            
        def win(p):
            # Check rows, columns, and diagonals for a winning line
            for i in range(3):
                if all(board[i][j] == p for j in range(3)):
                    return True
                if all(board[j][i] == p for j in range(3)):
                    return True
            if all(board[i][i] == p for i in range(3)):
                return True
            if all(board[i][2 - i] == p for i in range(3)):
                return True
            return False
            
        x_win = win('X')
        o_win = win('O')
        
        # Both players cannot win simultaneously
        if x_win and o_win:
            return False
        # If X wins, X must have played the last move
        if x_win and x_count != o_count + 1:
            return False
        # If O wins, O must have played the last move
        if o_win and x_count != o_count:
            return False
            
        return True
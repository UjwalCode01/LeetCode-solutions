class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board or not board[0]:
            return 0
        
        rows, cols = len(board), len(board[0])
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X':
                    # Check if cell above is 'X'
                    if r > 0 and board[r - 1][c] == 'X':
                        continue
                    # Check if cell to the left is 'X'
                    if c > 0 and board[r][c - 1] == 'X':
                        continue
                    
                    # It's the top-left corner of a battleship
                    count += 1
                    
        return count
from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        n = len(board)
        target = n * n

        def get_coords(num):
            idx = num - 1
            row_from_bottom = idx // n
            r = (n - 1) - row_from_bottom
            col_in_row = idx % n
            c = col_in_row if row_from_bottom % 2 == 0 else (n - 1) - col_in_row
            return r, c

        visited = set([1])
        queue = deque([(1, 0)])

        while queue:
            curr, rolls = queue.popleft()
            if curr == target:
                return rolls

            for nxt in range(curr + 1, min(curr + 6, target) + 1):
                r, c = get_coords(nxt)
                dest = board[r][c] if board[r][c] != -1 else nxt
                if dest not in visited:
                    visited.add(dest)
                    queue.append((dest, rolls + 1))

        return -1
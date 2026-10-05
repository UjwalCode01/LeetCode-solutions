from collections import deque
import re

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(s: str) -> str:
            # Recursively collapse 3 or more consecutive identical balls
            rx = re.compile(r'(\w)\1{2,}')
            while True:
                s, count = rx.subn('', s)
                if count == 0:
                    break
            return s

        # Hand sorted for consistent state representation
        hand = "".join(sorted(hand))
        queue = deque([(board, hand, 0)])
        visited = set([(board, hand)])

        while queue:
            curr_board, curr_hand, steps = queue.popleft()

            if not curr_board:
                return steps

            # Iterate over all possible insertion indices and available hand balls
            for i in range(len(curr_board) + 1):
                for j in range(len(curr_hand)):
                    # Avoid duplicate insertions of identical balls in hand
                    if j > 0 and curr_hand[j] == curr_hand[j - 1]:
                        continue

                    # Essential Rule for Zuma:
                    # 1. Insert if same color matches adjacent character
                    # 2. Insert if placing BETWEEN two identical characters (even if different color!)
                    ball = curr_hand[j]
                    
                    same_as_right = (i < len(curr_board) and curr_board[i] == ball)
                    same_as_left = (i > 0 and curr_board[i - 1] == ball)
                    between_same = (0 < i < len(curr_board) and curr_board[i - 1] == curr_board[i])

                    if not (same_as_right or same_as_left or between_same):
                        continue

                    next_board = clean(curr_board[:i] + ball + curr_board[i:])
                    next_hand = curr_hand[:j] + curr_hand[j + 1:]

                    if (next_board, next_hand) not in visited:
                        visited.add((next_board, next_hand))
                        queue.append((next_board, next_hand, steps + 1))

        return -1
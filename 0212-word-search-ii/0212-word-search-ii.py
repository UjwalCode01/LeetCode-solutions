class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # 1. Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        ROWS, COLS = len(board), len(board[0])
        result = []

        # 2. DFS function
        def dfs(r, c, node):
            char = board[r][c]
            curr_node = node.children[char]

            # If we matched a word, append it and clear to prevent duplicate finds
            if curr_node.word:
                result.append(curr_node.word)
                curr_node.word = None  

            # Mark visited
            board[r][c] = '#'

            # Explore 4-directional neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)

            # Backtrack
            board[r][c] = char

            # Optimization: Prune leaf nodes from Trie to save memory/search time
            if not curr_node.children:
                del node.children[char]

        # 3. Start search from each cell on the board
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return result
        
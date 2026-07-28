from collections import defaultdict, deque

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        words = set(wordList)
        if endWord not in words:
            return []

        # Store graph parents to backtrack paths later
        parents = defaultdict(set)
        # Store level/distance of each visited word
        level = {beginWord: 0}
        
        queue = deque([beginWord])
        found = False

        while queue and not found:
            # Process level by level
            current_level_visited = set()
            for _ in range(len(queue)):
                word = queue.popleft()
                curr_dist = level[word]

                # Try changing each character to 'a'-'z'
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == word[i]:
                            continue
                        next_word = word[:i] + c + word[i+1:]

                        if next_word in words:
                            # If encountered at next level
                            if next_word not in level:
                                level[next_word] = curr_dist + 1
                                parents[next_word].add(word)
                                current_level_visited.add(next_word)
                                if next_word == endWord:
                                    found = True
                            elif level[next_word] == curr_dist + 1:
                                parents[next_word].add(word)

            queue.extend(current_level_visited)

        if not found:
            return []

        # Backtrack with DFS from endWord to beginWord
        res = []

        def dfs(node, path):
            if node == beginWord:
                res.append(path[::-1])
                return
            for parent in parents[node]:
                dfs(parent, path + [parent])

        dfs(endWord, [endWord])
        return res
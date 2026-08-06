class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(index, node):
            curr = node
            for i in range(index, len(word)):
                char = word[i]
                if char == '.':
                    # Check all possible child nodes
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.is_end_of_word

        return dfs(0, self.root)
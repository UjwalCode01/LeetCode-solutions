class WordFilter:

    def __init__(self, words: list[str]):
        self.woo = {}
        for index, word in enumerate(words):
            length = len(word)
            # Generate all possible suffixes and prefixes
            for i in range(min(10, length + 1)):
                suff = word[:i]
                for j in range(min(10, length + 1)):
                    pref = word[length - j:]
                    self.woo[suff + '#' + pref] = index

    def f(self, pref: str, suff: str) -> int:
        # Query format is suff + '#' + pref based on how we stored it
        query = pref + '#' + suff
        return self.woo.get(query, -1)
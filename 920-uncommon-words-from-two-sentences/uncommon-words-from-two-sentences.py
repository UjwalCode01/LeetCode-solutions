from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        counts = Counter(s1.split() + s2.split())
        return [word for word, freq in counts.items() if freq == 1]
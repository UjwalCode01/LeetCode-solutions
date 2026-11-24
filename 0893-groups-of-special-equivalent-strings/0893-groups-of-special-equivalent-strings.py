class Solution(object):
    def numSpecialEquivGroups(self, words):
        groups = set()

        for word in words:
            even_chars = tuple(sorted(word[0::2]))
            odd_chars = tuple(sorted(word[1::2]))
            groups.add((even_chars, odd_chars))

        return len(groups)
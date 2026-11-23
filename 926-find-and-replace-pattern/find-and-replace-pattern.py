class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def encode(s):
            seen = {}
            res = []
            for i, ch in enumerate(s):
                if ch not in seen:
                    seen[ch] = i
                res.append(seen[ch])
            return res

        target = encode(pattern)
        return [w for w in words if len(w) == len(pattern) and encode(w) == target]
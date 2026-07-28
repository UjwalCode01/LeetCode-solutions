class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word_set = set(wordDict)
        memo = {}

        def backtrack(idx):
            # If subproblem already solved, return cached result
            if idx in memo:
                return memo[idx]

            # Base case: reached the end of string
            if idx == len(s):
                return [""]

            res = []
            for i in range(idx + 1, len(s) + 1):
                word = s[idx:i]
                if word in word_set:
                    # Recursively get all valid sentences for the suffix
                    sub_sentences = backtrack(i)
                    for sub in sub_sentences:
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)

            memo[idx] = res
            return res

        return backtrack(0)
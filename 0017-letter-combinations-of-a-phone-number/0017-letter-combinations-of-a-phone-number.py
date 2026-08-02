class Solution(object):
    def letterCombinations(self, digits):
        """:type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []

        def backtrack(index, current_combination):
            # Base case: reached the end of digits string
            if index == len(digits):
                res.append(current_combination)
                return

            # Explore all possible letters for the current digit
            for letter in phone_map[digits[index]]:
                backtrack(index + 1, current_combination + letter)

        backtrack(0, "")
        return res
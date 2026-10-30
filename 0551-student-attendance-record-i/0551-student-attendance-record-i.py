class Solution:
    def checkRecord(self, s: str) -> bool:
        # Check if absent count is less than 2 and 'LLL' is not a substring
        return s.count('A') < 2 and 'LLL' not in s
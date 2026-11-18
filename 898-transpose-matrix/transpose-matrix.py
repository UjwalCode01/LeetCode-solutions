class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        # Using zip to unpack rows as columns, then converting back to lists
        return [list(row) for row in zip(*matrix)]
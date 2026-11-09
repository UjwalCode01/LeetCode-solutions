class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        res = []
        for row in image:
            # Reverse the row horizontally and invert each bit (1 - x)
            inverted_row = [1 - x for x in row[::-1]]
            res.append(inverted_row)
        return res
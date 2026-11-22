class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        total = rows * cols
        res = [[rStart, cStart]]
        if total == 1:
            return res

        r, c = rStart, cStart
        steps = 1
        dir_idx = 0

        while len(res) < total:
            for _ in range(2):
                dr, dc = directions[dir_idx]
                for _ in range(steps):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                        if len(res) == total:
                            return res
                dir_idx = (dir_idx + 1) % 4
            steps += 1

        return res
class Solution(object):
    def superEggDrop(self, k, n):
        f = [0] * (k + 1)
        moves = 0
        while f[k] < n:
            moves += 1
            for eggs in range(k, 0, -1):
                f[eggs] += f[eggs - 1] + 1
        return moves
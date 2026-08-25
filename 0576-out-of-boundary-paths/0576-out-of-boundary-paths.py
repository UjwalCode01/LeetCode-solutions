class Solution(object):

  def findPaths(self, m, n, maxMove, startRow, startColumn):
    """:type m: int

    :type n: int
    :type maxMove: int
    :type startRow: int
    :type startColumn: int
    :rtype: int
    """
    MOD = 10**9 + 7
    memo = {}

    def dfs(r, c, moves):
      # If out of boundary, 1 valid path found
      if r < 0 or r >= m or c < 0 or c >= n:
        return 1
      # If no moves left, no path out
      if moves == 0:
        return 0

      state = (r, c, moves)
      if state in memo:
        return memo[state]

      # Explore all 4 directions
      paths = (
          dfs(r + 1, c, moves - 1)
          + dfs(r - 1, c, moves - 1)
          + dfs(r, c + 1, moves - 1)
          + dfs(r, c - 1, moves - 1)
      ) % MOD

      memo[state] = paths
      return paths

    return dfs(startRow, startColumn, maxMove)
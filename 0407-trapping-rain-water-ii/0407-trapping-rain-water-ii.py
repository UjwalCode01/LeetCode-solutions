import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []

        # Step 1: Add all border cells to the min-heap
        for r in range(m):
            for c in range(n):
                if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        water = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2: Expand inward starting from the lowest boundary cell
        while heap:
            h, r, c = heapq.heappop(heap)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # Trapped water is the height difference, if any
                    water += max(0, h - heightMap[nr][nc])
                    # Push to heap with the maximum height seen so far
                    heapq.heappush(heap, (max(heightMap[nr][nc], h), nr, nc))

        return water
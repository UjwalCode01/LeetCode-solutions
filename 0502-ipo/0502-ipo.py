import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        # Pair (capital, profit) and sort by capital required
        projects = sorted(zip(capital, profits))
        max_heap = []
        i = 0
        n = len(projects)

        for _ in range(k):
            # Push all affordable projects into max_heap
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])  # Max-heap via negation
                i += 1

            # If no affordable projects are available, stop early
            if not max_heap:
                break

            # Pick project with maximum profit
            w += -heapq.heappop(max_heap)

        return w
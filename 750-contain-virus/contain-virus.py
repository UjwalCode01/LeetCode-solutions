class Solution:
    def containVirus(self, isInfected: list[list[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        total_walls = 0
        
        while True:
            # Step 1: Identify all infected regions, their walls needed, and threatened uninfected cells
            regions = []
            frontier = []
            walls_used = []
            visited = set()
            
            for r in range(m):
                for c in range(n):
                    if isInfected[r][c] == 1 and (r, c) not in visited:
                        # BFS to find the connected component
                        q = [(r, c)]
                        visited.add((r, c))
                        region = {(r, c)}
                        f = set()
                        walls = 0
                        
                        while q:
                            curr_r, curr_c = q.pop(0)
                            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                nr, nc = curr_r + dr, curr_c + dc
                                if 0 <= nr < m and 0 <= nc < n:
                                    if isInfected[nr][nc] == 1 and (nr, nc) not in visited:
                                        visited.add((nr, nc))
                                        q.append((nr, nc))
                                        region.add((nr, nc))
                                    elif isInfected[nr][nc] == 0:
                                        f.add((nr, nc))
                                        walls += 1
                        regions.append(region)
                        frontier.append(f)
                        walls_used.append(walls)
            
            # If there are no infected regions left, we are done
            if not regions:
                break
                
            # Step 2: Find the region that threatens the most uninfected cells
            max_threat_idx = 0
            for i in range(1, len(regions)):
                if len(frontier[i]) > len(frontier[max_threat_idx]):
                    max_threat_idx = i
            
            # If the most threatening region doesn't threaten any uninfected cells, stop
            if not frontier[max_threat_idx]:
                break
                
            # Step 3: Quarantine the most threatening region by adding its walls and turning it to -1
            total_walls += walls_used[max_threat_idx]
            for r, c in regions[max_threat_idx]:
                isInfected[r][c] = -1 # Mark as quarantined
                
            # Step 4: Let all other regions spread to their adjacent uninfected cells
            for i in range(len(regions)):
                if i == max_threat_idx:
                    continue
                for r, c in frontier[i]:
                    isInfected[r][c] = 1
                    
        return total_walls
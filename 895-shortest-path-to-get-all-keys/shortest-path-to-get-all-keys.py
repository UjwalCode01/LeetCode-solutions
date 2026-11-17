from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        m, n = len(grid), len(grid[0])
        start_r, start_c = 0, 0
        total_keys = 0
        
        # Step 1: Locate the starting point and count total keys
        for r in range(m):
            for c in range(n):
                cell = grid[r][c]
                if cell == '@':
                    start_r, start_c = r, c
                elif 'a' <= cell <= 'z':
                    total_keys += 1
                    
        # Target bitmask representing all keys collected
        target_mask = (1 << total_keys) - 1
        
        # Queue stores tuples of (row, col, key_mask, steps)
        queue = deque([(start_r, start_c, 0, 0)])
        visited = {(start_r, start_c, 0)}
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, mask, steps = queue.popleft()
            
            # If all keys are collected, return the steps
            if mask == target_mask:
                return steps
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    cell = grid[nr][nc]
                    
                    # If it's a wall, skip
                    if cell == '#':
                        continue
                        
                    new_mask = mask
                    
                    # If it's a lock, check if we have the corresponding key
                    if 'A' <= cell <= 'Z':
                        key_index = ord(cell) - ord('A')
                        if not (mask & (1 << key_index)):
                            continue # Don't have the key yet
                            
                    # If it's a key, add it to our bitmask
                    elif 'a' <= cell <= 'z':
                        key_index = ord(cell) - ord('a')
                        new_mask |= (1 << key_index)
                        
                    # If this state hasn't been visited, add it to queue
                    state = (nr, nc, new_mask)
                    if state not in visited:
                        visited.add(state)
                        queue.append((nr, nc, new_mask, steps + 1))
                        
        return -1
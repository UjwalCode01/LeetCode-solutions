from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        # Queue stores tuples of (position, speed)
        queue = deque([(0, 1)])
        # Visited set to avoid redundant states
        visited = set([(0, 1)])
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                pos, speed = queue.popleft()
                
                # If we reach the target, return the number of steps
                if pos == target:
                    return steps
                
                # Option 1: 'A' (Accelerate)
                next_pos = pos + speed
                next_speed = speed * 2
                # Pruning: only explore if position doesn't overshoot unreasonably
                if (next_pos, next_speed) not in visited and abs(target - next_pos) < target:
                    visited.add((next_pos, next_speed))
                    queue.append((next_pos, next_speed))
                
                # Option 2: 'R' (Reverse)
                reverse_speed = -1 if speed > 0 else 1
                if (pos, reverse_speed) not in visited and abs(target - pos) < target:
                    visited.add((pos, reverse_speed))
                    queue.append((pos, reverse_speed))
            
            steps += 1
            
        return -1
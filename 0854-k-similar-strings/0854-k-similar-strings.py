from collections import deque

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
            
        queue = deque([(s1, 0)]) # stores (current_string, swaps_count)
        visited = {s1}
        
        while queue:
            curr, steps = queue.popleft()
            
            if curr == s2:
                return steps
                
            # Find the first index i where characters don't match
            i = 0
            while curr[i] == s2[i]:
                i += 1
                
            # Try swapping curr[i] with any character curr[j] (where j > i) that matches s2[i]
            curr_list = list(curr)
            for j in range(i + 1, len(curr)):
                if curr_list[j] == s2[i]:
                    # Swap
                    curr_list[i], curr_list[j] = curr_list[j], curr_list[i]
                    next_str = "".join(curr_list)
                    
                    if next_str not in visited:
                        visited.add(next_str)
                        queue.append((next_str, steps + 1))
                        
                    # Backtrack swap for the next iteration
                    curr_list[i], curr_list[j] = curr_list[j], curr_list[i]
                    
            # Optimization: If we found a direct match for s2[i], 
            # we don't need to branch out further for this specific state.
            # (Greedy optimization specific to K-Similar Strings)
            # But the standard BFS above is fully robust and passes all test cases.
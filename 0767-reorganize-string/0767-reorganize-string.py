from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count character frequencies
        count = Counter(s)
        
        # Max heap stores (-frequency, char)
        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)
        
        res = []
        prev_freq, prev_char = 0, ''
        
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            res.append(char)
            
            # If the previous character still has remaining count, push it back into the heap
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
                
            # Current character becomes the previous character for the next iteration
            prev_freq, prev_char = freq + 1, char # Increment because frequencies are negative
            
        result_str = "".join(res)
        
        # If length doesn't match, it means it's impossible to reorganize
        return result_str if len(result_str) == len(s) else ""
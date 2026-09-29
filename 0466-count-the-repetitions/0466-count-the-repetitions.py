class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        # Map: s2_index -> (s1_count, s2_count)
        recall = {}
        
        s1_count, s2_count = 0, 0
        s2_idx = 0
        
        while s1_count < n1:
            s1_count += 1
            
            # Process one full copy of s1
            for char in s1:
                if char == s2[s2_idx]:
                    s2_idx += 1
                    if s2_idx == len(s2):
                        s2_count += 1
                        s2_idx = 0
            
            # Check if cycle exists
            if s2_idx in recall:
                prev_s1_count, prev_s2_count = recall[s2_idx]
                
                # Length of the cycle
                cycle_s1 = s1_count - prev_s1_count
                cycle_s2 = s2_count - prev_s2_count
                
                # How many full cycles fit in the remaining s1 copies
                num_cycles = (n1 - s1_count) // cycle_s1
                
                # Fast-forward counters
                s1_count += num_cycles * cycle_s1
                s2_count += num_cycles * cycle_s2
                
            else:
                recall[s2_idx] = (s1_count, s2_count)
                
        # Total s2 occurrences divided by n2 gives the max 'm'
        return s2_count // n2
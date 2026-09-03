class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # Sort the pairs based on their end elements
        pairs.sort(key=lambda x: x[1])
        
        current_end = float('-inf')
        chain_length = 0
        
        for p in pairs:
            if p[0] > current_end:
                current_end = p[1]
                chain_length += 1
                
        return chain_length
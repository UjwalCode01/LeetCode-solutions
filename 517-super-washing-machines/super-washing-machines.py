class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        total = sum(machines)
        n = len(machines)
        
        if total % n != 0:
            return -1
            
        target = total // n
        max_moves = 0
        curr_balance = 0
        
        for dresses in machines:
            # Net difference for current machine
            diff = dresses - target
            
            # Cumulative balance of dresses transferred across the current split
            curr_balance += diff
            
            # Constraints:
            # 1. |curr_balance|: dresses that must cross this partition boundary
            # 2. diff: single machine offloading limit (can only give 1 dress per move)
            max_moves = max(max_moves, abs(curr_balance), diff)
            
        return max_moves
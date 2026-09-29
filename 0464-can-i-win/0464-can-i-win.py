class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        # If desired total is non-positive, first player wins immediately
        if desiredTotal <= 0:
            return True

        # Sum of all available integers
        total_sum = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2
        
        # If total sum is less than desiredTotal, no one can win
        if total_sum < desiredTotal:
            return False

        memo = {}

        def can_win(used_mask, remaining_total):
            # If state already computed, return cached result
            if used_mask in memo:
                return memo[used_mask]

            for i in range(maxChoosableInteger):
                # Check if i-th number (value i + 1) is not used yet
                if not (used_mask & (1 << i)):
                    val = i + 1
                    
                    # If picking this number reaches the goal
                    # OR forces the next player into a losing position
                    if val >= remaining_total or not can_win(used_mask | (1 << i), remaining_total - val):
                        memo[used_mask] = True
                        return True

            memo[used_mask] = False
            return False

        return can_win(0, desiredTotal)
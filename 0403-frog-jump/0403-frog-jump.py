class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        # Quick edge case check: Pehli jump mandatory 1 unit ki hai.
        # Agar second stone 1 position par nahi hai, toh aage nahi ja sakte.
        if stones[1] != 1:
            return False
        
        # Hash map: stone_position -> set of jump sizes (k) that reached this stone
        mark = {stone: set() for stone in stones}
        mark[0].add(0) # Start position
        
        for stone in stones:
            for k in mark[stone]:
                # Next possible jumps: k - 1, k, k + 1
                for step in (k - 1, k, k + 1):
                    if step > 0 and (stone + step) in mark:
                        mark[stone + step].add(step)
        
        # Last stone tak pahunchne ke liye koi valid jump hai ya nahi
        return len(mark[stones[-1]]) > 0
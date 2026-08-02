class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(start, target, path):
            # Base Case 1: Valid combination found
            if len(path) == k and target == 0:
                res.append(list(path))
                return
            
            # Base Case 2: Invalid path (too many elements or sum exceeded)
            if len(path) > k or target < 0:
                return
            
            # Try numbers from current 'start' to 9
            for i in range(start, 10):
                # Backtracking step: Choose, Recurse, Backtrack
                path.append(i)
                backtrack(i + 1, target - i, path)
                path.pop()  # Undo the choice
                
        backtrack(1, n, [])
        return res
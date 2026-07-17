class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        # 1. Sort the candidates to easily skip duplicates
        candidates.sort()
        
        def backtrack(start, target, path):
            # Base case: if target is met, add the current path to results
            if target == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                # If the current number exceeds the remaining target, stop the loop (pruning)
                if candidates[i] > target:
                    break
                
                # Skip duplicate elements at the same decision level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Make a choice
                path.append(candidates[i])
                
                # Move to the next element (i + 1 ensures each number is used only once)
                backtrack(i + 1, target - candidates[i], path)
                
                # Undo the choice (backtrack)
                path.pop()
                
        backtrack(0, target, [])
        return res
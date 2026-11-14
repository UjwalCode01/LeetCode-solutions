import collections

class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        n = len(quiet)
        
        # answer[i] = will store the least quiet person richer than or as rich as person i
        # Use a value like -1 as a placeholder to indicate the result is not yet calculated.
        self.answer = [-1] * n
        
        # Build the graph: richerThan[i] contains people who are directly richer than i.
        self.richer_than = collections.defaultdict(list)
        for rich_p, poor_p in richer:
            self.richer_than[poor_p].append(rich_p)
        
        # Global variable to access in dfs
        self.quietness = quiet

        # Recursive function with memoization
        def dfs(i):
            # If already calculated, return the result
            if self.answer[i] != -1:
                return self.answer[i]
            
            # 1. Base case idea: initially, the best is person i themselves
            self.answer[i] = i
            
            # 2. Recursive step: Look at everyone directly richer than person i
            for j in self.richer_than[i]:
                # Ask: "Who is the quietest among people who are richer than my rich friend j?"
                candidate = dfs(j)
                
                # Compare that candidate with the quietest person I currently know.
                # Agar ye candidate quietest value rakhta hai, to answer update karo.
                # (Yahan logic complete kiya gaya hai jahan pehle colon missing tha)
                if self.quietness[candidate] < self.quietness[self.answer[i]]:
                    self.answer[i] = candidate
            
            # Store and return the calculated result
            return self.answer[i]
        
        # Call the dfs function for every person to ensure we calculate for everyone
        for i in range(n):
            dfs(i)
        
        return self.answer
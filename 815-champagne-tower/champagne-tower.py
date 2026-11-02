class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Initial row array jisme top glass par saara poured champagne daal rahe hain
        tower = [poured]
        
        for row in range(query_row):
            next_row = [0.0] * (len(tower) + 1)
            for glass in range(len(tower)):
                # Agar glass overflow kar raha hai ( capacity 1.0 se zyada hai )
                if tower[glass] > 1.0:
                    overflow = (tower[glass] - 1.0) / 2.0
                    next_row[glass] += overflow
                    next_row[glass + 1] += overflow
            tower = next_row
            
        # Target glass mein maximum 1.0 hi hold ho sakta hai
        return min(1.0, tower[query_glass])
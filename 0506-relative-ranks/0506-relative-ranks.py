class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # Step 1: Sort scores in descending order to identify top performers
        sorted_scores = sorted(score, reverse=True)
        
        # Step 2: Create a rank map for quick lookup
        rank_map = {}
        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank_map[s] = "Gold Medal"
            elif i == 1:
                rank_map[s] = "Silver Medal"
            elif i == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(i + 1)
                
        # Step 3: Map original scores to their assigned rank
        return [rank_map[s] for s in score]
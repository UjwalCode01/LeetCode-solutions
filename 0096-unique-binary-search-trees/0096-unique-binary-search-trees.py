class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i] will store the number of unique BSTs with i nodes
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1
        dp[1] = 1
        
        # Build solution from 2 to n nodes
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                left_subtrees = dp[root - 1]
                right_subtrees = dp[nodes - root]
                
                dp[nodes] += left_subtrees * right_subtrees
                
        return dp[n]
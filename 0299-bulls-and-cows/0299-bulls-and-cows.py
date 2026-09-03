class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cows = 0
        
        # Secret aur guess ke digits ke frequency ko track karne ke liye array (0-9)
        secret_count = [0] * 10
        guess_count = [0] * 10
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[int(s)] += 1
                guess_count[int(g)] += 1
                
        # Cows ke liye minimum matches count karenge across both frequencies
        for i in range(10):
            cows += min(secret_count[i], guess_count[i])
            
        return "{}A{}B".format(bulls, cows)
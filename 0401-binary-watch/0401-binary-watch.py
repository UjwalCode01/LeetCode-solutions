class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        result = []
        
        # Iterate over all possible hours (0 to 11) and minutes (0 to 59)
        for h in range(12):
            for m in range(60):
                # Count total set bits for the current hour and minute
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    result.append("{}:{:02d}".format(h, m))
                    
        return result
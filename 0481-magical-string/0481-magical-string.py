class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 3:
            return 1
            
        # Initialize with the base magical string
        s = [1, 2, 2]
        
        # Pointer for reading the counts of consecutive characters to generate
        head = 2
        
        # Generate elements until the string reaches length n
        while len(s) < n:
            # The next element to append alternates between 1 and 2
            next_num = 3 - s[-1]
            # The number of times to append is determined by s[head]
            count = s[head]
            
            for _ in range(count):
                s.append(next_num)
                
            head += 1
            
        # Count the number of '1's in the first n elements
        return s[:n].count(1)
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        head = 1
        step = 1
        left_to_right = True
        remaining = n

        while remaining > 1:
            # Update head if moving left-to-right OR if moving right-to-left with an odd count
            if left_to_right or remaining % 2 == 1:
                head += step
            
            # Halve remaining numbers, double step distance, and switch direction
            remaining //= 2
            step *= 2
            left_to_right = not left_to_right

        return head
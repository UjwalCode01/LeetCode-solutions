class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(num: int) -> bool:
            if num < 2:
                return False
            if num % 2 == 0:
                return num == 2
            d = 3
            while d * d <= num:
                if num % d == 0:
                    return False
                d += 2
            return True

        # Edge case: if n is small, check up to 11
        if n <= 2:
            return 2
        if n <= 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if n <= 11:
            return 11

        # Generate palindromes by mirroring roots (e.g., root 12 -> 121)
        # We start generating from the appropriate root length
        for length in range(1, 6):
            # Generate odd-length palindromes
            for root in range(10**(length - 1), 10**length):
                s = str(root)
                palindrome = int(s + s[:-1][::-1])
                if palindrome >= n and is_prime(palindrome):
                    return palindrome
            
            # Generate even-length palindromes (except for 10^8 constraints, but handled safely)
            for root in range(10**(length - 1), 10**length):
                s = str(root)
                palindrome = int(s + s[::-1])
                if palindrome >= n and is_prime(palindrome):
                    return palindrome
                    
        return -1
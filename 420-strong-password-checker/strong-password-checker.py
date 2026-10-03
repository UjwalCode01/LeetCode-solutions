class Solution(object):
    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """
        n = len(password)
        
        # Count missing types
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing_types = (not has_lower) + (not has_upper) + (not has_digit)
        
        # Find consecutive repeating character lengths
        repeats = []
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            length = j - i
            if length >= 3:
                repeats.append(length)
            i = j
            
        # Case 1: Length < 6
        if n < 6:
            return max(6 - n, missing_types)
        
        # Case 2: 6 <= Length <= 20
        elif n <= 20:
            replace_cnt = sum(l // 3 for l in repeats)
            return max(replace_cnt, missing_types)
        
        # Case 3: Length > 20
        else:
            delete_cnt = n - 20
            
            # Use deletions greedily to eliminate replacement needs
            # 1. Lengths with len % 3 == 0 (costs 1 delete to reduce 1 replace)
            for idx in range(len(repeats)):
                if delete_cnt > 0 and repeats[idx] % 3 == 0:
                    repeats[idx] -= 1
                    delete_cnt -= 1
            
            # 2. Lengths with len % 3 == 1 (costs 2 deletes to reduce 1 replace)
            for idx in range(len(repeats)):
                if delete_cnt > 1 and repeats[idx] % 3 == 1:
                    repeats[idx] -= 2
                    delete_cnt -= 2
            
            # 3. Any remaining length >= 3 (costs 3 deletes to reduce 1 replace)
            for idx in range(len(repeats)):
                if delete_cnt > 0 and repeats[idx] >= 3:
                    d = min(delete_cnt, repeats[idx] - 2)
                    repeats[idx] -= d
                    delete_cnt -= d
            
            replace_cnt = sum(l // 3 for l in repeats)
            return (n - 20) + max(replace_cnt, missing_types)
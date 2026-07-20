class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seen_digit = False
        seen_dot = False
        seen_exponent = False
        
        for i, char in enumerate(s):
            # 1. Agar character ek digit hai
            if char.isdigit():
                seen_digit = True
                
            # 2. Agar character sign (+ ya -) hai
            elif char in ('+', '-'):
                # Sign ya toh index 0 par ho sakta hai, ya fir exponent ke just baad
                if i > 0 and s[i - 1] not in ('e', 'E'):
                    return False
                    
            # 3. Agar character dot (.) hai
            elif char == '.':
                # Dot pehle nahi aaya hona chahiye, aur exponent ke baad dot nahi ho sakta
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
                
            # 4. Agar character exponent (e ya E) hai
            elif char in ('e', 'E'):
                # Exponent pehle nahi aaya hona chahiye, aur isse pehle ek digit zaroori hai
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                # Exponent ke baad hume naye digits chahiye, isliye reset kar rahe hain
                seen_digit = False
                
            # 5. Agar koi bhi aur unkown character dikhe (jaise 'a', 'b', etc.)
            else:
                return False
                
        # Poora loop khatam hone ke baad, aakhri status valid digit par rukna chahiye
        return seen_digit
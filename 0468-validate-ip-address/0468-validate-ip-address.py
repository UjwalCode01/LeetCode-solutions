class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4(s: str) -> bool:
            parts = s.split('.')
            if len(parts) != 4:
                return False
            for p in parts:
                if not p.isdigit():
                    return False
                if len(p) > 1 and p[0] == '0':  # No leading zeros allowed
                    return False
                if not (0 <= int(p) <= 255):
                    return False
            return True

        def isIPv6(s: str) -> bool:
            parts = s.split(':')
            if len(parts) != 8:
                return False
            hexdigits = '0123456789abcdefABCDEF'
            for p in parts:
                if not (1 <= len(p) <= 4):
                    return False
                if not all(c in hexdigits for c in p):
                    return False
            return True

        if isIPv4(queryIP):
            return "IPv4"
        if isIPv6(queryIP):
            return "IPv6"
        return "Neither"